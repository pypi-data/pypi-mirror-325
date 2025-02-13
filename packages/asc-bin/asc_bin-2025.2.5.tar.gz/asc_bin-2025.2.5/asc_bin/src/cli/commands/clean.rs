use clap::Args;

use tracing;

use crate::{
    config::{self, project::ProjectConfig, relative_paths},
    errors::ErrorTag,
    util,
};

#[derive(Args, Debug, Clone)]
/// clean .asc and target dir
pub struct CleanArgs {}

impl CleanArgs {
    pub fn exec(&self) -> bool {
        match config::project::ProjectConfig::read_project_conf() {
            None => {
                tracing::error!(error_tag = ErrorTag::InvalidProjectError.as_ref(),);
                return false;
            }
            Some(project_conf) => {
                if project_conf.workspace.is_some() {
                    return self.clean_workspace(&project_conf);
                } else {
                    return self.clean_package(&project_conf);
                }
            }
        }
    }

    fn clean_package(&self, project_conf: &ProjectConfig) -> bool {
        let mut has_error = false;

        let cwd = util::fs::get_cwd();
        for bin in &project_conf.bins {
            util::fs::set_cwd(&format!(
                "{}/{}",
                relative_paths::ASC_PROJECT_DIR_NAME,
                bin.name
            ));
            tracing::info!(message = "clean bin", name = bin.name);

            // cmake
            has_error &= relative_paths::clean_cmake_files(&bin.name);

            // graph
            has_error &= relative_paths::clean_graph_files();

            util::fs::set_cwd("..");
            util::fs::remove_dir(&bin.name);

            util::fs::set_cwd(&cwd);
        }
        for lib in &project_conf.libs {
            util::fs::set_cwd(&format!(
                "{}/{}",
                relative_paths::ASC_PROJECT_DIR_NAME,
                lib.name
            ));
            tracing::info!(message = "clean lib", name = lib.name);

            // cmake
            has_error &= relative_paths::clean_cmake_files(&lib.name);

            // graph
            has_error &= relative_paths::clean_graph_files();

            util::fs::set_cwd("..");
            util::fs::remove_dir(&lib.name);

            util::fs::set_cwd(&cwd);
        }

        // cmake
        util::fs::set_cwd(relative_paths::ASC_PROJECT_DIR_NAME);
        has_error = relative_paths::clean_cmake_files("");
        util::fs::set_cwd(&cwd);

        // target
        has_error &= relative_paths::clean_target_files();

        return has_error;
    }

    fn clean_workspace(&self, package_conf: &config::project::ProjectConfig) -> bool {
        tracing::info!(message = "clean workspace", name = util::fs::get_cwd_name());

        let cwd = util::fs::get_cwd();

        // members
        let mut has_error = false;
        match &package_conf.workspace {
            None => {
                has_error &= true;
                tracing::error!(error_tag = ErrorTag::InvalidProjectWorkspaceError.as_ref(),);
            }
            Some(workspace_config) => {
                if workspace_config.members.is_empty() {
                    has_error &= true;
                    tracing::error!(error_tag = ErrorTag::InvalidProjectWorkspaceError.as_ref(),);
                }
                for m in &workspace_config.members {
                    if let Some(project_conf) = config::project::ProjectConfig::load(
                        &format!("{}/{}/{}", cwd, m, relative_paths::ASC_TOML_FILE_NAME),
                        false,
                    ) {
                        has_error &= self.clean_package(&project_conf);
                    }
                }
            }
        }

        // cmake
        util::fs::set_cwd(relative_paths::ASC_PROJECT_DIR_NAME);
        has_error &= relative_paths::clean_cmake_files("");
        util::fs::set_cwd(&cwd);

        // target
        has_error &= relative_paths::clean_target_files();

        return has_error;
    }
}
