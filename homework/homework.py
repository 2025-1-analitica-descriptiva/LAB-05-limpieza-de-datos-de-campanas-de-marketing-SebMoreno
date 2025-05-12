"""
Escriba el codigo que ejecute la accion solicitada.
"""


# pylint: disable=import-outside-toplevel


def clean_campaign_data():
    """
    En esta tarea se le pide que limpie los datos de una campaña de
    marketing realizada por un banco, la cual tiene como fin la
    recolección de datos de clientes para ofrecerls un préstamo.

    La información recolectada se encuentra en la carpeta
    files/input/ en varios archivos csv.zip comprimidos para ahorrar
    espacio en disco.

    Usted debe procesar directamente los archivos comprimidos (sin
    descomprimirlos). Se desea partir la data en tres archivos csv
    (sin comprimir): client.csv, campaign.csv y economics.csv.
    Cada archivo debe tener las columnas indicadas.

    Los tres archivos generados se almacenarán en la carpeta files/output/.

    client.csv:
    - client_id
    - age
    - job: se debe cambiar el "." por "" y el "-" por "_"
    - marital
    - education: se debe cambiar "." por "_" y "unknown" por pd.NA
    - credit_default: convertir a "yes" a 1 y cualquier otro valor a 0
    - mortage: convertir a "yes" a 1 y cualquier otro valor a 0

    campaign.csv:
    - client_id
    - number_contacts
    - contact_duration
    - previous_campaing_contacts
    - previous_outcome: cmabiar "success" por 1, y cualquier otro valor a 0
    - campaign_outcome: cambiar "yes" por 1 y cualquier otro valor a 0
    - last_contact_day: crear un valor con el formato "YYYY-MM-DD",
        combinando los campos "day" y "month" con el año 2022.

    economics.csv:
    - client_id
    - const_price_idx
    - eurobor_three_months



    """
    import os
    import pandas as pd

    def set_binary(value):
        return lambda x: 1 if str(x).lower() == value else 0

    input_dir = "files/input/"
    output_dir = "files/output/"
    os.makedirs(output_dir, exist_ok=True)
    df = pd.concat((pd.read_csv(os.path.join(input_dir, file), compression="zip") for file in os.listdir(input_dir)), ignore_index=True)

    df["job"] = df["job"].str.replace(".", "").str.replace("-", "_")
    df["education"] = df["education"].str.replace(".", "_").replace("unknown", pd.NA)
    df["credit_default"] = df["credit_default"].apply(set_binary("yes"))
    df["mortgage"] = df["mortgage"].apply(set_binary("yes"))
    df["previous_outcome"] = df["previous_outcome"].apply(set_binary("success"))
    df["campaign_outcome"] = df["campaign_outcome"].apply(set_binary("yes"))
    df["last_contact_date"] = pd.to_datetime(df["day"].astype(str) + "-" + df["month"] + "-2022", format="%d-%b-%Y")

    client = df[["client_id", "age", "job", "marital", "education", "credit_default", "mortgage"]]
    campaign = df[["client_id", "number_contacts", "contact_duration", "previous_campaign_contacts", "previous_outcome", "campaign_outcome", "last_contact_date"]]
    economics = df[["client_id", "cons_price_idx", "euribor_three_months"]]

    client.to_csv(os.path.join(output_dir, "client.csv"), index=False)
    campaign.to_csv(os.path.join(output_dir, "campaign.csv"), index=False)
    economics.to_csv(os.path.join(output_dir, "economics.csv"), index=False)


if __name__ == "__main__":
    clean_campaign_data()
