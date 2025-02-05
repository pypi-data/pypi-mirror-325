# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [0.1.3] - 2025-02-04
### Fixed
- Fixed dependencies

## [0.1.2] - 2025-02-04
### Fixed
- Fixed dependencies

## [0.1.1] - 2025-02-04
### Added
- Add docstrings

## [0.1.0] - 2025-02-04
### Changed
- Start following [SemVer](https://semver.org) properly.
- Implement a buffer in the stream_response method of the AsyncAIssociateClient
- Make the event parser more robust by properly separating multiple events when they appear in a single chunk. 

### Added
- Add EventSource model for the raw received event.
- Add Message and Error for AI:ssociate specific data models inside EventSource's data field.

## [0.0.1] - 2025-01-30
### Added

- **AsyncAIssociateClient**: Add the first async client for the AI:ssociate API to this library.
- **Documentation**: Add a short description and instructions on how to install and use the library and the client which can be found in the [README.md](https://gitlab.com/christophsonntag/aissociate-python/-/blob/main/README.md)