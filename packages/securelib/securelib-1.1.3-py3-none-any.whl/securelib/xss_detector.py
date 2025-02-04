def detect_xss(payload: str) -> bool:
    dangerous_patterns = ["<script>", "onerror=", "alert("]
    return any(pattern in payload for pattern in dangerous_patterns)
