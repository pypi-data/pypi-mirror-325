[Compare the full difference.](https://github.com/callowayproject/bump-my-version/compare/0.31.1...0.32.0)

### Fixes

- Refactor CLI config-file option to use @config_option decorator. [cd06cbd](https://github.com/callowayproject/bump-my-version/commit/cd06cbda61e54eea05b27eda734efc956d81a28a)
    
  Replaced the manual `--config-file` option setup with the `@config_option` decorator for cleaner and reusable configuration management. This change simplifies the code and enhances maintainability by consolidating the configuration logic.
### New

- Added pytest-localserver as a test dependency. [c84243d](https://github.com/callowayproject/bump-my-version/commit/c84243dba710feebdb571b93ea3cfb120703fd4e)
    
- Add ConfigOption for flexible configuration. [1625248](https://github.com/callowayproject/bump-my-version/commit/1625248c492c8719d6591af38d3ae2799e9f168f)
    
  Introduce `ConfigOption` and related utilities in `bumpversion.click_config` to handle configuration file paths or URLs. Includes tests for processing options, resolving paths/URLs, and handling errors in `resolve_conf_location` and `download_url`.
- Added httpx as a dependency. [450154e](https://github.com/callowayproject/bump-my-version/commit/450154ea19a321e0de44ef764e029abaafd1535a)
    
### Other

- [pre-commit.ci] pre-commit autoupdate. [17e8301](https://github.com/callowayproject/bump-my-version/commit/17e8301e5a3750b349c97cebcbcc5953f32f9af1)
    
  **updates:** - [github.com/astral-sh/ruff-pre-commit: v0.9.3 → v0.9.4](https://github.com/astral-sh/ruff-pre-commit/compare/v0.9.3...v0.9.4)

- Bump actions/setup-python in the github-actions group. [c0771b0](https://github.com/callowayproject/bump-my-version/commit/c0771b029073feb6a2a3c5e35170f25879b97bc0)
    
  Bumps the github-actions group with 1 update: [actions/setup-python](https://github.com/actions/setup-python).


  Updates `actions/setup-python` from 5.3.0 to 5.4.0
  - [Release notes](https://github.com/actions/setup-python/releases)
  - [Commits](https://github.com/actions/setup-python/compare/v5.3.0...v5.4.0)

  ---
  **updated-dependencies:** - dependency-name: actions/setup-python
dependency-type: direct:production
update-type: version-update:semver-minor
dependency-group: github-actions

  **signed-off-by:** dependabot[bot] <support@github.com>

### Updates

- Updated other subcommands with the new config_option. [279838a](https://github.com/callowayproject/bump-my-version/commit/279838af100dbf3ffc84f500710967944af05f46)
    
- Improve config resolution and add error handling for paths. [43f0435](https://github.com/callowayproject/bump-my-version/commit/43f04357788bfc11bec4c087e69366f8ba38c3e6)
    
  Refactor `process_value` to handle `None` values and raise a `BumpVersionError` for non-existent files. Update related tests to ensure correct behavior for missing, existing, and URL-based config paths. These changes enhance robustness and user feedback in handling configuration inputs.
