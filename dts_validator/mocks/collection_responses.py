SAMPLE_COLLECTION_RESPONSES = [
    {
        "request_args": {"id": "general"},
        "response_payload": {
            "@context": "https://distributed-text-services.github.io/"
            "specifications/context/1.0.0draft-2.json",
            "@id": "general",
            "@type": "Collection",
            "totalItems": 2,
            "totalParents": 0,
            "totalChildren": 2,
            "title": "Collection Générale de l'École Nationale des Chartes",
            "dublincore": {
                "publisher": [
                    "École Nationale des Chartes",
                    "https://viaf.org/viaf/167874585",
                ],
                "title": [{
                    "lang": "fr",
                    "value": "Collection Générale de l'École Nationale"
                    "des Chartes",
                }],
            },
            "member": [
                {
                    "@id": "cartulaires",
                    "title": "Cartulaires",
                    "description": "Collection de cartulaires "
                    "d'Île-de-France et de ses environs",
                    "@type": "Collection",
                    "totalItems": 10,
                    "totalParents": 1,
                    "totalChildren": 10,
                },
                {
                    "@id": "lasciva_roma",
                    "title": "Lasciva Roma",
                    "description": "Collection of primary sources of interest"
                    " in the studies of Ancient World's sexuality",
                    "@type": "Collection",
                    "totalItems": 1,
                    "totalParents": 1,
                    "totalChildren": 1,
                },
                {
                    "@id": "lettres_de_poilus",
                    "title": "Correspondance des poilus",
                    "description": "Collection de lettres de poilus entre"
                    " 1917 et 1918",
                    "@type": "Collection",
                    "totalItems": 10000,
                    "totalParents": 1,
                    "totalChildren": 10000,
                },
            ],
        },
    },
    {
        "request_args": {"id": "lasciva_roma"},
        "response_payload": {
            # "@context":
            #     {
            #         "hydra": "https://www.w3.org/ns/hydra/core#",
            #         "dct": "http://purl.org/dc/terms/",
            #         "dts": "https://w3id.org/dts/api#",
            #         "lang": "@language",
            #         "value": "@value",
            #         "dublinCore": {
            #             "@id": "dts:dublinCore",
            #             "@context": {
            #                 "@vocab": "http://purl.org/dc/terms/"
            #             }
            #         },
            #     },
            "@context": "https://distributed-text-services.github.io/"
            "specifications/context/1.0.0draft-2.json",
            "@id": "lasciva_roma",
            "@type": "Collection",
            "totalItems": 3,
            "totalParents": 1,
            "totalChildren": 3,
            "title": "Lasciva Roma",
            "description": "Collection of primary sources of interest in "
            "the studies of Ancient World's sexuality",
            "dts:dublincore": {
                "creator": [
                    "Thibault Clérice",
                    "http://orcid.org/0000-0003-1852-9204",
                ],
                "title": [
                    {"lang": "la", "value": "Lasciva Roma"},
                ],
                "description": [{
                    "lang": "en",
                    "value": "Collection of primary sources of interest "
                    "in the studies of Ancient World's sexuality",
                }],
            },
            "member": [{
                "@id": "urn:cts:latinLit:phi1103.phi001",
                "title": "Priapeia",
                "dublincore": {
                    "type": ["http://chs.harvard.edu/xmlns/cts#work"],
                    "creator": [{"lang": "en", "value": "Anonymous"}],
                    "language": ["la", "en"],
                    "description": [
                        {"lang": "en", "value": "Anonymous lascivious Poems"}
                    ],
                },
                "@type": "Collection",
                "totalItems": 1,
                "totalParents": 1,
                "totalChildren": 1,
            }],
        },
        "validation_result": "",
    },
]
