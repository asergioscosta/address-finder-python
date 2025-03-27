import requests
import requests.exceptions


def buscar_endereco(cep):
    url = f'https://brasilapi.com.br/api/cep/v2/{cep}'

    try:
        response = requests.get(url)

        response.raise_for_status()

        dados = response.json()

        print("\n Endereço encontrado")
        print(f"CEP: {dados.get('cep')}")
        print(f"Rua: {dados.get('street')}")
        print(f"Bairro: {dados.get('neighborhood')}")
        print(f"Cidade: {dados.get('city')}")
        print(f"Estado: {dados.get('state')}")

    except requests.exceptions.HTTPError:
        print("CEP não encontrado ou inválido.")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API: {e}")

if __name__ == "__main__":
    print("Buscar endereço pelo CEP")

    cep = input("Digite em CEP (somente números): ").strip()

    cep = cep.replace("-", "").replace("", "")

    if len(cep) == 8 and cep.isdigit():
        buscar_endereco(cep)
    else:
        print("CEP inválido. Digite novamente o CEP com 8 dígitos.")
