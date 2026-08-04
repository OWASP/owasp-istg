# Versioning Guide

## Version Structure

The version structure for this project is defined as follows:

1. **MAJOR version:** Major versions consolidate extensive changes to multiple parts of the guide (for example, framework changes, multiple new or updated [components or component specializations](./src/02_framework/methodology.md#structure-of-the-catalog-of-test-cases), or substantially deeper coverage across many test cases).
2. **MINOR version:** Minor versions are released when a [component or component specialization](./src/02_framework/methodology.md#structure-of-the-catalog-of-test-cases) is added or extensively updated or refined.
3. **PATCH version:** Patch version releases are used for smaller fixes (bugs, typos, issues).

Each release will be tagged with a version identifier "*v[MAJOR].[MINOR].[PATCH]*".



## Development and Release Flow

The project uses trunk-based development:

- **`main`:** The working branch containing merged changes, including changes not yet released.
- **Release tags:** Stable releases are commits on `main` tagged with their version identifier.
- **Contribution branches:** Use short-lived, descriptive branches for individual changes. A branch that adds or updates a [component or component specialization](./src/02_framework/methodology.md#structure-of-the-catalog-of-test-cases) may use the `istg-[component_id]` pattern.

Finished changes merge into `main` through pull requests. The repository does not use a separate `latest` working branch; release tags identify the commits published as stable guide versions.
