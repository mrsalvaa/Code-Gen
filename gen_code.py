import secrets


def generar_codigo_recuperacion() -> str:
    # 64 caracteres hex = 32 bytes de entropía real
    hex_str = secrets.token_hex(32) 

    # Agrupar de a 4 caracteres
    grupos = [hex_str[i:i + 4] for i in range(0, len(hex_str), 4)]
    return " ".join(grupos)


if __name__ == "__main__":
    codigo = generar_codigo_recuperacion()
    print(codigo)
