# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2025-12-05

### Added
- Trace visualization support with 8 new fields for enhanced observability:
  - `environment` - Deployment environment tracking (production, staging, etc.)
  - `region` - Cloud region identifier with auto-detection
  - `credential_alias` - Human-readable API key identification
  - `trace_type` - Workflow category identifier for grouping
  - `trace_name` - Human-readable trace labels
  - `parent_transaction_id` - Distributed tracing support
  - `transaction_name` - Operation-level naming
  - `operation_subtype` - Additional operation detail (auto-detected)
- New `trace_fields.py` module for trace field capture and validation
- Comprehensive trace visualization example (`examples/trace_visualization_example.py`)
- Support for both environment variables and `usage_metadata` parameters for trace fields
- Auto-detection of environment and region from common cloud provider env vars

### Changed
- Updated `revenium_middleware` dependency to >=0.3.5
- Enhanced README with trace visualization fields documentation
- Updated `.env.example` with trace visualization field examples and comments

### Documentation
- Added "Trace Visualization Fields (v0.2.0+)" section to README
- Added comprehensive trace visualization example with 5 scenarios
- Updated `.env.example` with detailed trace field documentation

## [0.1.18] - 2025-11-17

### Documentation
- Added virtual environment setup instructions to examples/README.md
- Added dependency installation step
- Renumbered existing setup steps for clarity

## [0.1.17] - 2025-11-01

### Added
- Transaction ID exposure in responses via `_revenium_transaction_id` attribute
- Support for `response_quality_score` metadata field
- Examples for transaction ID usage

### Changed
- Updated examples documentation
- Improved README documentation

## [0.1.16] - 2025-09-12

### Added
- Middleware source to usage metadata
- CODE_OF_CONDUCT.md
- CONTRIBUTING.md
- SECURITY.md

### Changed
- Updated revenium_middleware dependency
- Improved documentation structure

## [0.1.15] - 2025-09-14

### Fixed
- Request timestamp inconsistency

## [0.1.14] - 2025-09-12

### Added
- Middleware source to usage metadata

### Changed
- Updated revenium_middleware dependency

## [0.1.13] - 2025-09-11

### Changed
- Updated dependency requirements

## [0.1.12] - 2025-09-10

### Added
- Nested subscriber metadata structure

### Changed
- Cost fields handling

## [0.1.11] - 2025-09-09

### Added
- Standardized documentation files
- CODE_OF_CONDUCT.md
- CONTRIBUTING.md
- SECURITY.md

## [0.1.10] - 2025-09-08

### Changed
- Updated subscriber handling
- Aligned with OpenAI middleware structure

## [0.1.9] - 2025-09-07

### Changed
- Updated documentation

## [0.1.8] - 2025-09-06

### Changed
- Updated dependencies

[Unreleased]: https://github.com/revenium/revenium-middleware-ollama-python/compare/v0.1.17...HEAD
[0.1.17]: https://github.com/revenium/revenium-middleware-ollama-python/compare/v0.1.16...v0.1.17
[0.1.16]: https://github.com/revenium/revenium-middleware-ollama-python/compare/v0.1.15...v0.1.16
[0.1.15]: https://github.com/revenium/revenium-middleware-ollama-python/compare/v0.1.14...v0.1.15
[0.1.14]: https://github.com/revenium/revenium-middleware-ollama-python/compare/v0.1.13...v0.1.14
[0.1.13]: https://github.com/revenium/revenium-middleware-ollama-python/compare/v0.1.12...v0.1.13
[0.1.12]: https://github.com/revenium/revenium-middleware-ollama-python/compare/v0.1.11...v0.1.12
[0.1.11]: https://github.com/revenium/revenium-middleware-ollama-python/compare/v0.1.10...v0.1.11
[0.1.10]: https://github.com/revenium/revenium-middleware-ollama-python/compare/v0.1.9...v0.1.10
[0.1.9]: https://github.com/revenium/revenium-middleware-ollama-python/compare/v0.1.8...v0.1.9
[0.1.8]: https://github.com/revenium/revenium-middleware-ollama-python/releases/tag/v0.1.8
