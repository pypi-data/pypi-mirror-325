# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] - 2024-12-22
### Added
- Quantum key generation process using Qiskit.
- Noise simulation for quantum channels with configurable noise intensity and types.
- Error detection and correction mechanisms using parity checks and hashing.
- Classical communication module for basis reconciliation and error correction.
- Full BB84 protocol implementation, including basis reconciliation and key sifting.
- Visualization tools for qubit states, measurement results, and noise impact.
- Customizable parameters for key length, noise, and error correction.

### Changed
- Initial release with full BB84 protocol implementation and supportive tools.

### Fixed
- N/A (Initial release)

## [1.1.0] - 2025-02-06
### Added
- Realistic quantum noise models (depolarizing, amplitude damping, phase damping).
- Free-space and fiber-optic QKD simulation.
- Multi-party QKD support for secure group communication.
- Quantum error correction using Shor Code and Steane Code.
- AI-based eavesdropping detection using anomaly detection.
- Integration with IBM Qiskit quantum devices.
- Enhanced real-time visualization of QKD exchange and error rates.
- Post-quantum cryptographic compatibility with lattice-based encryption.
- Key rate optimization for better performance.
- Device-independent QKD implementation.

### Fixed
- Improved error correction efficiency.
- Addressed deprecated Qiskit function calls.
