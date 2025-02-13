use std::collections::{BTreeMap, BTreeSet};

use crate::{
    cli::commands::VcpkgArgs,
    config::{
        self,
        project::{DependencyConfig, PackageConfig},
        relative_paths::{self, ASC_TOML_FILE_NAME, VCPKG_JSON_FILE_NAME},
        vcpkg::{
            port::{VcpkgDependency, VcpkgDependencyDesc, VcpkgJsonDependency, VcpkgPortJson},
            port_manifest::VcpkgPortManifest,
            registry_manifest::{VcpkgConfiguration, VcpkgDefaultRegistry, VcpkgRegistry},
            versions_baseline::{VcpkgBaseline, VcpkgPortVersion},
            versions_port::{VcpkgPortTreeVersion, VcpkgPortVersions},
        },
    },
    git::{
        self,
        log::{GitCommitInfo, GIT_LOG_FORMAT_COMMIT_HASH_DATE},
    },
};

use super::index::VcpkgSearchIndex;

static VCPKG_PORT_NAME_KEY: &str = "name";
static VCPKG_PORT_PLATFORM_KEY: &str = "platform";
static VCPKG_FEATURE_PLATFORM_DELIMITER: &str = "@";
static VCPKG_REGISTRY_KIND_GIT: &str = "git";

pub fn gen_vcpkg_configurations(dependencies: &BTreeMap<String, DependencyConfig>) {
    // group ports
    let mut grouped_ports = BTreeMap::new();

    // set dependencies
    let mut vcpkg_data = VcpkgDependency::load(relative_paths::VCPKG_JSON_FILE_NAME, true).unwrap();
    vcpkg_data.dependencies.clear();
    vcpkg_data.overrides.clear();

    // set registries
    let vcpkg_args = VcpkgArgs::load_or_default();
    let mut registry_baseline = BTreeMap::new();

    for (registry, url, branch, vcpkg_root_dir) in vcpkg_args.flatten_registry() {
        let search_index = VcpkgSearchIndex::load(
            &config::system_paths::DataPath::vcpkg_search_index_json(
                vcpkg_args.index_directory.as_ref().unwrap(),
                &registry,
            ),
            true,
        )
        .unwrap();

        for (port_name, desc) in dependencies {
            let mut dep = VcpkgDependencyDesc::default();
            dep.name =
                VcpkgPortManifest::normalize_port_name(format!("{port_name}-{}", desc.version));
            if !desc.features.is_empty() {
                dep.default_features = Some(false);
            }
            for f in &desc.features {
                match f.split_once(VCPKG_FEATURE_PLATFORM_DELIMITER) {
                    None => {
                        dep.features.push(BTreeMap::from([(
                            String::from(VCPKG_PORT_NAME_KEY),
                            f.clone(),
                        )]));
                    }
                    Some((n, p)) => {
                        dep.features.push(BTreeMap::from([
                            (String::from(VCPKG_PORT_NAME_KEY), n.to_string()),
                            (String::from(VCPKG_PORT_PLATFORM_KEY), p.to_string()),
                        ]));
                    }
                };
            }
            vcpkg_data.dependencies.push(dep);

            if let Some(versions) = search_index.versions.get(port_name) {
                if versions.contains(&desc.version) {
                    grouped_ports
                        .entry(registry.clone())
                        .or_insert_with(BTreeSet::new)
                        .insert(VcpkgPortManifest::normalize_port_name(format!(
                            "{port_name}-{}",
                            desc.version
                        )));
                } else {
                    tracing::warn!("can't found {port_name} which version = {}", desc.version)
                }
            }
        }

        // set registry
        let commit = git::log::get_latest_commit(&vcpkg_root_dir, GIT_LOG_FORMAT_COMMIT_HASH_DATE);
        registry_baseline.insert(registry, (url, branch, commit.hash));
    }

    if vcpkg_data.dependencies.is_empty() {
        tracing::error!("can't found any dependencies in {}", ASC_TOML_FILE_NAME);
    } else {
        // write vcpkg.json
        vcpkg_data.dump(true, false);

        // auto bootstrap
        super::bootstrap::run();
    }

    if registry_baseline.is_empty() {
        if !vcpkg_data.dependencies.is_empty() {
            tracing::error!("can't found all dependencies in same baseline");
        }
    } else {
        let mut vcpkg_conf_data =
            VcpkgConfiguration::load(relative_paths::VCPKG_CONFIGURATION_JSON_FILE_NAME, true)
                .unwrap();
        vcpkg_conf_data.registries.clear();
        for (registry, (url, branch, hash)) in registry_baseline {
            if registry == config::relative_paths::VCPKG_DIR_NAME {
                vcpkg_conf_data.default_registry = VcpkgDefaultRegistry {
                    kind: String::from(VCPKG_REGISTRY_KIND_GIT),
                    repository: url,
                    baseline: hash.clone(),
                };
            } else {
                vcpkg_conf_data.registries.push(VcpkgRegistry {
                    kind: String::from(VCPKG_REGISTRY_KIND_GIT),
                    reference: branch,
                    repository: url,
                    baseline: hash.clone(),
                    packages: grouped_ports
                        .get(&registry)
                        .unwrap_or(&BTreeSet::new())
                        .iter()
                        .map(|s| s.clone())
                        .collect::<Vec<String>>(),
                    ..Default::default()
                });
            }
        }
        // write vcpkg-configuration.json
        vcpkg_conf_data.dump(true, false);
    }
}

pub fn gen_port_json(
    repo_root_dir: &String,
    package_conf: &PackageConfig,
    dependencies: &BTreeMap<String, DependencyConfig>,
    latest_commit: &GitCommitInfo,
) -> (bool, u32) {
    let mut data = VcpkgPortJson::load(
        &config::system_paths::DataPath::vcpkg_ports_vcpkg_json_path(
            repo_root_dir,
            &package_conf.name,
        ),
        true,
    )
    .unwrap();

    let port_file_cmake = std::fs::read_to_string(
        &config::system_paths::DataPath::vcpkg_ports_port_file_cmake_path(
            repo_root_dir,
            &package_conf.name,
        ),
    )
    .unwrap_or_default();

    data.name = package_conf.name.clone();
    if data.version >= package_conf.version {
        tracing::error!(
            message = format!("version in {VCPKG_JSON_FILE_NAME} was large than package version in {ASC_TOML_FILE_NAME}"),
            version_in_vcpkg_json = data.version,
            version_in_asc_toml = data.version,
        );
        return (false, data.port_version);
    } else if data.version == package_conf.version {
        if port_file_cmake.contains(&latest_commit.hash) {
            tracing::warn!(
                message = "the version and commit hash were not changed",
                version = data.version,
                commit_hash = latest_commit.hash,
                commit_time = latest_commit.date_time
            );

            println!("Do you want to update port version, yes or no? ");
            let mut choose = String::new();
            std::io::stdin().read_line(&mut choose).unwrap();
            if [String::from("y"), String::from("yes")].contains(&choose.to_lowercase()) {
                data.port_version += 1;
                update_vcpkg_json_fields(&mut data, package_conf, dependencies);
                data.dump(true, false);
                return (true, data.port_version);
            }

            return (false, data.port_version);
        } else {
            tracing::warn!(
                message = "the version was not changed, but commit hash was changed",
                version = data.version,
                commit_hash = latest_commit.hash,
                commit_time = latest_commit.date_time
            );

            println!("Do you want to update port version, yes or no? ");
            let mut choose = String::new();
            std::io::stdin().read_line(&mut choose).unwrap();
            if [String::from("y"), String::from("yes")].contains(&choose.to_lowercase()) {
                data.port_version += 1;
                update_vcpkg_json_fields(&mut data, package_conf, dependencies);
                data.dump(true, false);
                return (true, data.port_version);
            }

            tracing::error!(
                message = format!("update package version in {ASC_TOML_FILE_NAME} first"),
                version = data.version,
                commit_hash = latest_commit.hash,
                commit_time = latest_commit.date_time
            );
            return (false, data.port_version);
        }
    } else {
        data.version = package_conf.version.clone();
        data.port_version = 0;
        update_vcpkg_json_fields(&mut data, package_conf, dependencies);
        data.dump(true, false);
        return (true, data.port_version);
    }
}

fn update_vcpkg_json_fields(
    data: &mut VcpkgPortJson,
    package_conf: &PackageConfig,
    dependencies: &BTreeMap<String, DependencyConfig>,
) {
    data.description = package_conf.description.clone();
    data.homepage = package_conf.repository.clone();
    data.license = package_conf.license.clone();
    data.supports = package_conf.supports.clone();

    data.dependencies.clear();

    for (name, desc) in dependencies {
        let mut dep = VcpkgJsonDependency::default();
        dep.name = name.clone();
        let mut platforms = vec![];
        if !desc.features.is_empty() {
            dep.default_features = Some(false);
            for feat in &desc.features {
                match feat.split_once(VCPKG_FEATURE_PLATFORM_DELIMITER) {
                    None => {
                        dep.features.push(feat.clone());
                    }
                    Some((n, p)) => {
                        let ns = n.to_string();
                        if !dep.features.contains(&ns) {
                            dep.features.push(ns);
                        }
                        let ps = p.to_string();
                        if !platforms.contains(&ps) {
                            platforms.push(ps);
                        }
                    }
                };
            }
        }
        if !platforms.is_empty() {
            dep.platform = Some(
                platforms
                    .iter()
                    .map(|p| {
                        if p.contains("|") || p.contains("&") {
                            format!("({p})")
                        } else {
                            p.clone()
                        }
                    })
                    .collect::<Vec<String>>()
                    .join(" | "),
            );
        }
        data.dependencies.push(dep);

        data.dependencies.push(VcpkgJsonDependency {
            name: String::from("vcpkg-cmake"),
            host: Some(true),
            ..Default::default()
        });
        data.dependencies.push(VcpkgJsonDependency {
            name: String::from("vcpkg-cmake-config"),
            host: Some(true),
            ..Default::default()
        });
    }
}

pub fn gen_port_versions(
    repo_root_dir: &String,
    name: &str,
    version: &Option<String>,
    version_date: &Option<String>,
    version_semver: &Option<String>,
    version_string: &Option<String>,
    port_version: u32,
) -> bool {
    let mut versions_data = VcpkgPortVersions::load(
        &config::system_paths::DataPath::vcpkg_versions_port_json_path(repo_root_dir, name),
        true,
    )
    .unwrap();

    let mut baseline_version = String::new();
    for new_version_option in [version, version_date, version_semver, version_string] {
        if let Some(new_version) = new_version_option {
            baseline_version = new_version.clone();
            if !versions_data.versions.is_empty() {
                let old_tree_version = &versions_data.versions[0].clone();
                for old_version_option in [
                    &old_tree_version.version,
                    &old_tree_version.version_date,
                    &old_tree_version.version_semver,
                    &old_tree_version.version_string,
                ] {
                    if let Some(old_version) = old_version_option {
                        if old_version == new_version
                            && old_tree_version.port_version == port_version
                        {
                            tracing::warn!(
                                message = "the port version was not changed",
                                name = name,
                                version = new_version,
                                port_version = port_version,
                            );
                            versions_data.versions.clear();
                            break;
                        }
                    }
                }
            }
        }
    }

    versions_data.versions.insert(
        0,
        VcpkgPortTreeVersion {
            git_tree: git::rev_parse::run("HEAD", name, repo_root_dir),
            version: version.clone(),
            version_date: version_date.clone(),
            version_semver: version_semver.clone(),
            version_string: version_string.clone(),
            port_version: port_version,
            ..Default::default()
        },
    );

    let mut result = versions_data.dump(true, false);

    let mut baseline_data = VcpkgBaseline::load(
        &&config::system_paths::DataPath::vcpkg_versions_baseline_json_path(repo_root_dir),
        true,
    )
    .unwrap();
    if let Some(v) = baseline_data.default.get(name) {
        if v.baseline == baseline_version && v.port_version == port_version {
            tracing::warn!(
                message = "the baseline version was not changed",
                name = name,
                version = baseline_version,
                port_version = port_version,
            );
            return result;
        }
    }

    baseline_data.default.insert(
        name.to_string(),
        VcpkgPortVersion {
            baseline: baseline_version,
            port_version: port_version,
        },
    );

    result &= baseline_data.dump(true, false);

    return result;
}
