# ct001 - Post-Quantum Secure Cryptography Library 🚀

`ct001` is a next-generation **encryption and authentication library** designed for **post-quantum security**. Built with **AI-resistant cryptography**, this library ensures **highly secure and ephemeral authentication** without relying on traditional passwords, OTPs, or stored credentials.

## 🔐 Features:

- **Quantum-Resistant Encryption** – Uses advanced cryptographic techniques resistant to quantum attacks.
- **Self-Destructing Authentication** – Generates ephemeral encryption keys that cannot be reused or cloned.
- **Multi-Layer Security** – Protects against phishing, replay attacks, and AI-based security bypass attempts.
- **No Stored Credentials** – Ensures maximum security without the risk of stored passwords being exposed.

## 📦 Installation

```bash
pip install ct001
```

from ct001.encryption import PostQuantumCrypto

pqc = PostQuantumCrypto()
public_key = pqc.get_public_key()
private_key = pqc.get_private_key()

print("Public Key:", public_key.decode())
print("Private Key:", private_key.decode())
