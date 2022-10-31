import csv


def analyze_log(path_to_file):
    formato_csv = str(path_to_file).split(".")[-1]
    if formato_csv != "csv":
        raise FileNotFoundError(f"Extensão inválida:'{path_to_file}'")
    try:
        with open(path_to_file, encoding="utf8") as arquivo:
            ordens = []
            dados = csv.reader(arquivo, delimiter=",", quotechar='"')
            *data, = dados
            for orden in data:
                ordens.append(orden)
            return ordens
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente:'{path_to_file}'")
