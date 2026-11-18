import json
import unittest
from mcp_server import handle_mcp_request


class AnnaMcpQuantTests(unittest.TestCase):
    def test_tools_list(self) -> None:
        res = handle_mcp_request({"jsonrpc": "2.0", "id": 1, "method": "tools/list"})
        self.assertEqual(len(res["result"]["tools"]), 3)

    def test_call_scan_whale_flows(self) -> None:
        res = handle_mcp_request({
            "jsonrpc": "2.0",
            "id": 2,
            "method": "tools/call",
            "params": {"name": "scan_whale_flows", "arguments": {"chain": "solana"}},
        })
        self.assertFalse(res["result"]["isError"])
        data = json.loads(res["result"]["content"][0]["text"])
        self.assertEqual(data["chain"], "solana")


if __name__ == "__main__":
    unittest.main()
