# BB84 Simulation Library

A comprehensive Python library for simulating the **BB84 quantum key distribution protocol**, now enhanced with **AI-based eavesdropping detection, advanced noise models, Qiskit integration, and improved visualization tools.**

---

## **Features**
### **🔑 Complete BB84 Protocol**
- Qubit preparation, transmission, and measurement.
- Key sifting, error correction, and privacy amplification.

### **🔍 Advanced Eavesdropping & Security Features**
- Configurable noise models: depolarizing, amplitude damping, phase damping, and readout errors.
- **NEW:** AI-based eavesdropper detection using **Isolation Forest**.
- **NEW:** Simulated **lossy channel effects** on key transmission.

### **📊 Visualization Tools**
- Protocol workflow visualization.
- Noise impact visualization.
- Key sifting visualization.
- **NEW:** **Real-time QBER visualization** for intrusion detection.

### **💻 Quantum Execution**
- **NEW:** IBM **Qiskit Integration** for running BB84 on real quantum hardware.

### **🛠 Extensible & Modular Design**
- Modular architecture for easy integration of additional features.
- **NEW:** Caching for quantum noise models to optimize performance.

---

## **Installation**

### **Prerequisites**
- Python 3.8+
- pip package manager
- Install dependencies:
  ```bash
  pip install -r requirements.txt
