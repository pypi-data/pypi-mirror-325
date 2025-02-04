from solana.rpc.api import Client
from solana.transaction import Transaction
from solana.publickey import PublicKey
from solana.keypair import Keypair
from solana.system_program import transfer, TransferParams
from solana.rpc.types import TxOpts
from typing import Union
import json
from testnet.interfaces.logs import Logger


class SolanaTransaction:
    def __init__(self, rpc_url: str = "https://api.testnet.solana.com"):
        """
        Initializes the Solana client.
        :param rpc_url: URL of the RPC server (default: Testnet)
        """
        self._logger = Logger("solana-transactions.log").get_logger()
        self.client = Client(rpc_url)

    @staticmethod
    def load_keypair_from_hex(private_key: str) -> Keypair:
        """
        Loads a Keypair from a hex-encoded private key.
        :param private_key: Private key in hex format.
        :return: Keypair
        """
        secret_key = bytes.fromhex(private_key)
        return Keypair.from_secret_key(secret_key)

    def send_transaction(self, sender_keypair: Keypair, recipient_address: str, amount_sol: float) -> Union[str, dict]:
        try:
            recipient_pubkey = PublicKey(recipient_address)
            lamport = int(amount_sol * 1_000_000_000)

            # Get the latest blockhash
            blockhash_response = self.client.get_latest_blockhash()

            # Ensure the response is in the expected format
            if not blockhash_response or not blockhash_response.value or not blockhash_response.value.blockhash:
                return {"error": "Failed to fetch latest blockhash"}

            # Convert the blockhash to string
            recent_blockhash = str(blockhash_response.value.blockhash)

            # Create and sign transaction
            txn = Transaction(recent_blockhash=recent_blockhash).add(
                transfer(
                    TransferParams(
                        from_pubkey=sender_keypair.public_key,
                        to_pubkey=recipient_pubkey,
                        lamports=lamport
                    )
                )
            )

            # Send transaction with signature verification
            response = self.client.send_transaction(txn, sender_keypair, opts=TxOpts(skip_confirmation=False))
            if response:
                response = response.to_json()
                res = json.loads(response)["result"]
                url_transaction = f"https://explorer.solana.com/tx/{res}?cluster=testnet"
                self._logger.info(f"Successfully sent transaction: {url_transaction}")
                return url_transaction
            else:
                return {"error": "Failed to send transaction"}

        except Exception as e:
            return {"error": str(e)}
