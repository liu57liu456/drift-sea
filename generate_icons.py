"""Generate PWA icons — ocean-themed PNGs using stdlib only."""
import zlib
import struct
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SERVER_DIR = os.path.join(SCRIPT_DIR, "server")


def write_png(path, width, height):
    """Write a simple ocean-blue gradient PNG with a drift-bottle silhouette."""
    raw_rows = []
    for y in range(height):
        row = bytearray()
        row.append(0)  # filter: none
        for x in range(width):
            # Sky-to-ocean gradient
            ratio = y / height
            # Deep ocean blue at bottom, lighter sky blue at top
            r = int(10 + (160 - 10) * (1 - ratio))
            g = int(30 + (200 - 30) * (1 - ratio))
            b = int(60 + (230 - 60) * (1 - ratio))
            # Warm horizon line
            if 0.45 < ratio < 0.55:
                warmth = 1.0 - abs(ratio - 0.5) * 10
                r = int(r + 180 * warmth)
                g = int(g + 100 * warmth)
                b = int(b - 30 * warmth)
            # Bottle silhouette (simple bottle shape in the center)
            cx, cy = width // 2, height // 2
            dx, dy = abs(x - cx), abs(y - cy)
            if width >= 128:
                # Bottle body
                bottle_x = abs(x - cx) / (width * 0.08)
                bottle_y = (y - cy + height * 0.02) / (height * 0.25)
                if -1.0 <= bottle_y <= 1.0:
                    # Neck: thin at top, body: wider at bottom
                    if bottle_y < -0.3:
                        neck_width = 0.35  # narrow neck
                    else:
                        # Body widens
                        body_ratio = min((bottle_y + 0.3) / 1.3, 1.0)
                        neck_width = 0.35 + body_ratio * 0.65
                    if bottle_x <= neck_width:
                        # Draw bottle outline
                        bottle_edge = neck_width - bottle_x
                        if bottle_edge < 0.15:
                            # Edge highlight
                            r = min(255, r + 80)
                            g = min(255, g + 80)
                            b = min(255, b + 50)
                        elif bottle_x < neck_width - 0.15:
                            # Bottle interior — lighter
                            r = min(255, int(r * 1.3))
                            g = min(255, int(g * 1.3))
                            b = min(255, int(b * 1.3))
                # Cork at the very top
                cork_top = cy - height * 0.22
                cork_bottom = cy - height * 0.10
                if cork_top <= y <= cork_bottom and abs(x - cx) < width * 0.04:
                    r, g, b = 180, 140, 80
            r = max(0, min(255, r))
            g = max(0, min(255, g))
            b = max(0, min(255, b))
            row.extend([r, g, b])
        raw_rows.append(bytes(row))

    raw_data = b"".join(raw_rows)

    def chunk(ctype, data):
        c = ctype + data
        return struct.pack(">I", len(data)) + c + struct.pack(">I", zlib.crc32(c) & 0xFFFFFFFF)

    ihdr = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)  # 8-bit RGB
    png = b"\x89PNG\r\n\x1a\n"
    png += chunk(b"IHDR", ihdr)
    png += chunk(b"IDAT", zlib.compress(raw_data))
    png += chunk(b"IEND", b"")

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(png)
    print(f"  [OK] {path} ({width}x{height})")


if __name__ == "__main__":
    print("Generating PWA icons...")
    write_png(os.path.join(SERVER_DIR, "icon-192.png"), 192, 192)
    write_png(os.path.join(SERVER_DIR, "icon-512.png"), 512, 512)
    print("Done.")
