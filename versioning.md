# Versioning Guide

## Version Structure

The version structure for this project is defined as follows:

1. **MAJOR version:** Major versions consolidate extensive changes to multiple parts of the guide (e.g., framework changes, multiple new/updated [components / component specializations](./src/02_framework/methodology#structure-of-the-catalog-of-test-cases), greater depth of detail for a considerable amount of test cases).
2. **MINOR version:** Minor versions are released once a [components / component specializations](./src/02_framework/methodology#structure-of-the-catalog-of-test-cases) has been added or extensively updated/refined.
3. **PATCH version:** Patch version releases are used for smaller fixes (bugs, typos, issues). 

Each release will be tagged with a version identifier "*v[MAJOR].[MINOR].[PATCH]*".



## Branch Structure

The following branch structure has been defined:

- **main:** Latest release version
- **latest:** Main working branch that includes all finished but unreleased changes
- **istg-[component_id]:** Used for adding/updating parts of [components / component specializations](./src/02_framework/methodology#structure-of-the-catalog-of-test-cases)
- Further branches will be created for individual topics. Self-explanatory names should be used.