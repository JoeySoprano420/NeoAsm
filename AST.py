[
    # Map Declaration Node
    {
        "type": "map", 
        "identifier": "A", 
        "entries": [
            {"key": "src", "value": "RAM"}, 
            {"key": "dst", "value": "GPU"}
        ]
    },

    # Variable Declaration Node
    {
        "type": "variable", 
        "var_type": "INT", 
        "identifier": "temp", 
        "attributes": {
            "range": "0..255", 
            "check": "rigid"
        }
    },

    # AOT Declaration Node
    {
        "type": "AOT", 
        "identifier": "test", 
        "attributes": {
            "type": "STATIC", 
            "size": "1024"
        }
    },

    # Packetized Execution Declaration Node
    {
        "type": "packet", 
        "identifier": "data", 
        "attributes": {
            "size": "512", 
            "exec": "EXECUTE", 
            "priority": "RAM"
        }
    }
]

