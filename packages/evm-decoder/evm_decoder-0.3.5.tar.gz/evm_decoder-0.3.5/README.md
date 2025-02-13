# 🔍 EVM Decoder

A powerful Python toolkit for decoding and analyzing Ethereum Virtual Machine (EVM) transactions and events. This package provides three core managers for comprehensive blockchain data analysis.

## 🎯 Core Components

### 1. DecoderManager

The `DecoderManager` is responsible for decoding various types of blockchain data:

```python
from evm_decoder import DecoderManager

# Initialize with custom config or use default
decoder_manager = DecoderManager(config_path='path/to/config.json')

# Automatic decoding
result = decoder_manager.decode(event_data)

# Use specific decoder
result = decoder_manager.decode_with_specific_decoder(data, 'my_decoder')

# Add custom decoder
decoder_manager.add_decoder('custom_name', custom_decoder)
```

Key Features:
- 🔄 Automatic decoder selection based on input data
- 📚 Support for transaction and event decoding
- 🛠 Configurable through JSON configuration file
- 🔌 Extensible with custom decoders

### 2. AnalyzerManager

The `AnalyzerManager` provides deep analysis of transactions and their effects:

```python
from evm_decoder import AnalyzerManager

# Initialize analyzer
analyzer = AnalyzerManager()

# Analyze full transaction
analysis = analyzer.analyze_transaction(tx_with_logs)
# Returns:
# {
#     "balance_analysis": {...},  # Balance changes per address
#     "token_transfers": [...]     # Detailed token transfer events
# }

# Analyze specific aspects
token_transfers = analyzer.analyze_token_transfers(tx_with_logs)
balance_changes = analyzer.analyze_balance_changes(tx_with_logs)
```

Key Features:
- 💰 Track token transfers (ERC20, native currency)
- 📊 Analyze balance changes across addresses
- 🔄 Support for WETH wrapping/unwrapping events
- 🧮 Automatic balance calculation and reconciliation

### 3. ContractManager

The `ContractManager` handles all smart contract interactions:

```python
from evm_decoder import ContractManager

# Initialize with Web3 provider
contract_manager = ContractManager("https://mainnet.infura.io/v3/YOUR-KEY")

# Read contract data
result = contract_manager.read_contract(
    contract_type="erc20",
    address="0x...",
    method="balanceOf",
    args=["0x..."],
    block_identifier="latest"
)

# Write to contract
tx_hash = contract_manager.write_contract(
    contract_type="erc20",
    address="0x...",
    method="transfer",
    args=["0x...", 1000],
    private_key="your_private_key"
)

# Get contract instance
contract = contract_manager.get_contract("erc20", "0x...")
```

Key Features:
- 📚 Automatic ABI management
- 🔄 Contract instance caching
- 📖 Read contract data
- ✍️ Write contract transactions
- 🔐 Secure transaction signing

## 🚀 Installation

```bash
pip install -r requirements.txt
```

Required dependencies:
- `web3>=7.5.0`: For Ethereum node interaction
- `pandas`: For data manipulation
- `chain_index`: For chain information

## 📖 Configuration

Create a `decoder_config.json` file:

```json
{
    "transaction_decoders": [
        {
            "type": "transaction",
            "name": "erc20_transfer",
            "abi_path": "abis/erc20.json",
            "fixed_types": {
                "transfer": [
                    {"name": "to", "type": "address"},
                    {"name": "value", "type": "uint256"}
                ]
            }
        }
    ],
    "event_decoders": [
        {
            "type": "event",
            "name": "transfer_event",
            "abi_path": "abis/erc20.json"
        }
    ]
}
```

## 🤝 Contributing

We welcome contributions! Please check our contribution guidelines.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📬 Support

For support and questions:
- 📚 Check our documentation
- 🐛 Report issues on GitHub
- 💬 Join our community discussions

---

<p align="center">Built with ❤️ for the Ethereum community</p>