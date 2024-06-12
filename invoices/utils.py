import xml.etree.ElementTree as ET
import pandas as pd


def process_invoices(file_paths):
    conceptos = []

    for file_path in file_paths:
        tree = ET.parse(file_path)
        root = tree.getroot()
        namespaces = {
            "cfdi": "http://www.sat.gob.mx/cfd/4",
            "tfd": "http://www.sat.gob.mx/TimbreFiscalDigital",
        }
        comprobante_info = root.attrib
        emisor_info = root.find("cfdi:Emisor", namespaces).attrib
        receptor_info = root.find("cfdi:Receptor", namespaces).attrib

        for concepto in root.findall(
            "cfdi:Conceptos/cfdi:Concepto",
            namespaces,
        ):
            concepto_info = concepto.attrib
            concepto_info.update(comprobante_info)
            concepto_info.update(emisor_info)
            concepto_info.update(receptor_info)
            impuestos = concepto.find("cfdi:Impuestos", namespaces)
            traslados = []
            if impuestos is not None:
                for traslado in impuestos.findall(
                    "cfdi:Traslados/cfdi:Traslado", namespaces
                ):
                    traslados.append(traslado.attrib)
            concepto_info["importeImpuesto"] = traslado.get("Importe")
            if traslado.get("Impuesto") == "002":
                concepto_info["tipoImporteImpuesto"] = "IVA"
            if traslado.get("Impuesto") == "003":
                concepto_info["tipoImporteImpuesto"] = "IEPS"
            concepto_info["Impuestos"] = traslados
            conceptos.append(concepto_info)

    df_conceptos = pd.DataFrame(conceptos)
    df_conceptos = df_conceptos.convert_dtypes()
    cols = [
        "Cantidad",
        "Importe",
        "ValorUnitario",
        "SubTotal",
        "Total",
        "importeImpuesto",
    ]
    df_conceptos[cols] = df_conceptos[cols].apply(
        pd.to_numeric,
        errors="coerce",
    )
    return df_conceptos
