from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def transcriptie():
    """Deze functie transleert de opgegeven DNA-sequentie naar een
        aminozuursequentie.
        :param: DNA-sequentie
        :return: aminozuursequentie
        """
    dna_sequentie = request.args.get("dna", "")
    code = {'ttt': 'F', 'tct': 'S', 'tat': 'Y', 'tgt': 'C',
            'ttc': 'F', 'tcc': 'S', 'tac': 'Y', 'tgc': 'C',
            'tta': 'L', 'tca': 'S', 'taa': '*', 'tga': '*',
            'ttg': 'L', 'tcg': 'S', 'tag': '*', 'tgg': 'W',
            'ctt': 'L', 'cct': 'P', 'cat': 'H', 'cgt': 'R',
            'ctc': 'L', 'ccc': 'P', 'cac': 'H', 'cgc': 'R',
            'cta': 'L', 'cca': 'P', 'caa': 'Q', 'cga': 'R',
            'ctg': 'L', 'ccg': 'P', 'cag': 'Q', 'cgg': 'R',
            'att': 'I', 'act': 'T', 'aat': 'N', 'agt': 'S',
            'atc': 'I', 'acc': 'T', 'aac': 'N', 'agc': 'S',
            'ata': 'I', 'aca': 'T', 'aaa': 'K', 'aga': 'R',
            'atg': 'M', 'acg': 'T', 'aag': 'K', 'agg': 'R',
            'gtt': 'V', 'gct': 'A', 'gat': 'D', 'ggt': 'G',
            'gtc': 'V', 'gcc': 'A', 'gac': 'D', 'ggc': 'G',
            'gta': 'V', 'gca': 'A', 'gaa': 'E', 'gga': 'G',
            'gtg': 'V', 'gcg': 'A', 'gag': 'E', 'ggg': 'G'
            }
    aminozuursequentie = ""
    dna_sequentie_lower = dna_sequentie.lower()
    if "atg" in dna_sequentie_lower:
        if len(dna_sequentie_lower) % 3 == 0:
            for i in range(0, len(dna_sequentie_lower), 3):
                codon = dna_sequentie_lower[i:i + 3]
                if codon in code:
                    if code[codon] != "*":
                        aminozuursequentie += code[codon]
                    else:
                        return render_template("Afvinkopdract 2 HTML.html",
                                               dna=dna_sequentie_lower,
                                               aminozuursequentie=
                                               aminozuursequentie)
                else:
                    print(
                        "Het volgende codon kan niet getransleerd "
                        "worden omdat deze een letter bevat die geen A,"
                        " T, G of C is.")
        else:
            print(
                "Bij het maken van deze sequentie blijven losse "
                "nucleotiden over, geef een andere sequentie.")
    else:
        print(
            "Deze DNA-sequentie kan niet getransleerd worden tot "
            "aminozuursequentie omdat deze sequentie geen "
            "startcodon bevat")
    return render_template("Afvinkopdract 2 HTML.html",
                           dna=dna_sequentie_lower,
                           aminozuursequentie=aminozuursequentie)


if __name__ == '__main__':
    app.run()
