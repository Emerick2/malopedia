let ID = 1;
let mesDictionnaire=[]
let listeDeTousLesNoms=[];
let chargé = false;
let tempsI = 0;
const table = document.getElementById("évolution");

let évolution = [
    [1, 2, "Niveau 18"],
    [2, 3, "Niveau 38"],
    [4, 5, "Niveau 18"],
    [5, 6, "Niveau 38"],
    [7, 8, "Niveau 18"],
    [8, 9, "Niveau 38"],
    [10, 11, "Niveau 20 la nuit"],
    [11, 12, "Niveau 40 avec Madonde dans l'équipe"],
    [13, 14, "Niveau 20 le jour avec Amplégnée dans l'équipe"],
    [14, 15, "Niveau 40 après 5h passées dans l'équipe"],
    [16, 17, "Niveau 15"],
    [16, 18, "Avec l'objet feuille morte"],
    [16, 19, "Avec une pierre soleil"],
    [16, 20, "Avec l'objet grosse racine"],
    [26, 27, "Niveau 18"],
    [28, 29, "Niveau 12"],
    [30, 31, "Niveau 21"],
    [32, 33, "Niveau 32"],
    [33, 34, "Niveau 43"],
    [195, 197, "Niveau 22 avec une jolie feuille rouge"],
    [195, 37, "Avec une peau métal"],
    [195, 196, "Niveau 18 avec un estomat plain"],
    [196, 198, "Niveau 34"],
    [38, 39, "Niveau 26"],
    [39, 40, "Niveau 60 dans une grotte"],
    [39, 41, "Niveau 60 dans une jungle"],
    [42, 43, "Gagner un niveau dans une zone glacée"],
    [43, 44, "Niveau 32"],
    [45, 46, "Niveau 18"],
    [46, 47, "Niveau 33"],
    [48, 49, "Niveau 18"],
    [49, 50, "Niveau 40"],
    [51, 53, "Niveau 12 dans un jardin"],
    [51, 54, "Niveau 12 dans l'eau"],
    [51, 52, "Niveau 12 dans une grotte"],
    [52, 55, "Niveau 40 dans une grotte"],
    [56, 57, "Niveau 12 en creusant pour se nourir"],
    [56, 58, "Niveau 12 en sautant pour se nourir"],
    [59, 60, "Niveau 25 si ces un mâle"],
    [59, 61, "Niveau 18 si ces une femelle"],
    [62, 63, "Niveau 21"],
    [65, 66, "Niveau 26"],
    [67, 68, "Niveau 26"],
    [178, 179, "Niveau 26"],
    [69, 70, "Niveau 15"],
    [70, 71, "Niveau 29"],
    [70, 72, "Niveau 29 avec une grosse ampoule"],
    [73, 74, "Le faire s'attacher au dos de quelqu'un sans qu'il ne sans rende compte, pendent 6 heures d'affiler"],
    [75, 76, "Niveau 20"],
    [76, 77, "Niveau 35 pendant un concert"],
    [78, 79, "Niveau 31"],
    [80, 81, "Niveau 26"],
    [85, 86, "Niveau 20 avec la capacité tête de fer"],
    [87, 88, "Niveau 25"],
    [88, 89, "En étant dans des eau très profonde"],
    [95, 96, "Niveau 20 dans une ville"],
    [96, 97, "Niveau 48 dans une jungle"],
    [98, 99, "Sauver une vie"],
    [100, 101, "Niveau 34"],
    [226, 227, "Niveau 16"],
    [227, 228, "Niveau 45"],
    [108, 109, "Niveau 32"],
    [110, 111, "Niveau 32"],
    [210, 211, "Quand il ne peut plus avancer !"],
    [120, 121, "Quand il ne peut plus avancer !"],
    [125, 126, "Avec Vipombre dans l'équipe (fusion)"],
    [128, 129, "Niveau 25"],
    [132, 133, "Niveau 24"],
    [133, 134, "Niveau 42"],
    [207, 208, "Niveau 15"],
    [136, 137, "Niveau 65 en étant roi de sa tribu"],
    [141, 142, "Niveau 30"],
    [142, 143, "Passer 40 jours dans le Deusert"],
    [144, 145, "Niveau 22"],
    [90, 91, "Niveau 24"],
    [105, 106, "Niveau 20"],
    [106, 107, "Niveau 45 en visitant un temple légendaire"],
    [130, 131, "Niveau 39"],
    [138, 139, "Niveau 18"],
    [139, 140, "Niveau 35"],
    [152, 153, "Niveau 18"],
    [153, 154, "Niveau 38"],
    [193, 194, "Quand il a fait un oeuf et la fais éclore"],
    [190, 191, "Niveau 48 avec une pierre feu"],
    [191, 192, "Niveau 60 dans l'espace"],
    [201, 202, "Niveau 16"],
    [202, 203, "Niveau 34"],
    [237, 238, "Niveau 12"],
    [238, 239, "Niveau 32 avec 5 Biscolo dans l'équipe"],
    [223, 224, "Niveau 12 avec un score optimal en sécurité"],
    [218,219, "Niveau 15"],
    [220, 221, "Niveau 18"],
    [221, 222, "Niveau 41"],
    [240, 241, "Laisser dans l'équipe six mois sans le faire sortire"],
    [240, 242, "Niveau 25"],
    [204, 205, "Niveau 19"],
    [205, 206, "Niveau 58"],
    [102, 103, "Gagne un niveau à Espelette"],
    [103, 104, "Niveau 35"],
    [244, 245,"Niveau 15"],
    [212, 213, "Niveau 31"]
]
ChargerCSV();
function Suivant(opéréateur){
    if (!chargé) return;
    chargé=false;
    ID += opéréateur;
    if (ID < 1){
        ID = 1;
    }
    if (ID > mesDictionnaire.length) ID = mesDictionnaire.length;
    ChargerPesonnage();
    chargé=true;
}
function ErreurImage(img, nomImage, IDImage){
    img.onerror = function () {
        //console.warn("Image introuvable, on tente en JPG...");
        img.onerror = function () {
            //console.warn("Toujours pas... on tente avec -" + nomImage + " en PNG...");
            img.onerror = function () {
                //console.warn("Dernière tentative avec ' - " + nomImage + "' en PNG...");
                img.onerror = function () {
                    console.error("Toutes les tentatives ont échoué pour l'image ID " + IDImage);
                };
                img.src = "La liste des normeaux/De 1 à 300 !/" + TrouverNomImage(IDImage, " - " + nomImage, "png");
            };
            img.src = "La liste des normeaux/De 1 à 300 !/" + TrouverNomImage(IDImage, "-" + nomImage, "png");
        };
        img.src = "La liste des normeaux/De 1 à 300 !/" + TrouverNomImage(IDImage, "", "jpg");
    };
}
function ChargerPesonnage() {
    let img = document.getElementById("malomon");
    img.src = mesDictionnaire[ID-1]["image"];

    ErreurImage(img, mesDictionnaire[ID - 1]["nom"], mesDictionnaire[ID - 1]["ID"]);

    document.getElementById("nom").textContent = mesDictionnaire[ID-1]["nom"];
    let d = mesDictionnaire[ID - 1]["description"];
    if (d.startsWith('"')) d = d.substring(1);
    if (d.endsWith('"')) d = d.substring(0, d.length - 1);
    document.getElementById("description").textContent = d;
    document.getElementById("numéro").textContent = "N°"+String(ID);
    //console.log("types/" + mesDictionnaire[ID-1]["type1"] + ".png");
    if (mesDictionnaire[ID-1]["type1"] != "") document.getElementById("type1").src = "types/" + mesDictionnaire[ID - 1]["type1"]+".png";
    else document.getElementById("type1").src = "";
    if (mesDictionnaire[ID-1]["type2"]!="")document.getElementById("type2").src = "types/" + mesDictionnaire[ID - 1]["type2"]+".png";
    else document.getElementById("type2").src = "";
    PlacerLesEvolution();
}
function TrouverNomImage(numero, milieu, extension = "png") {
    let numeroFormate = String(numero).padStart(3, '0');
    return numeroFormate +milieu+ "." + extension;
}
function ChargerCSV(){
    fetch("myCSV.txt")
        .then(response => response.text())
        .then(data => {
            let lignes = data.trim().split("\n");
            let tableau = lignes.map(ligne => ligne.split(";"));
            // ATTENTION : index 0 pour la première ligne/colonne
            n = -1;
            for (let i = 0; i < tableau.length; i++) {
                if (tableau[i][1][0] != "N" || tableau[i][1][tableau[i][1].length-1] == "²"){
                    continue;
                }
                n++;
                dict={};
                dict["ID"]=n+1;
                dict["nom"] = tableau[i][2];
                listeDeTousLesNoms.push(tableau[i][2]);
                dict["description"] = tableau[i][5];
                dict["étimologie"] = tableau[i][3];
                dict["région"] = tableau[i][7];
                dict["spéciale"] = tableau[i][8];
                dict["image"] = "La liste des normeaux/De 1 à 300 !/" +TrouverNomImage(n+1,"","png");
                t = CoupeType(tableau[i][4]);
                dict["type1"] = t[0];
                dict["type2"] = t[1];
                mesDictionnaire.push(dict);
            }
            chargé = true;
            Suivant(0);
        })
        .catch(err => console.error("Erreur de lecture :", err));
}
function CoupeType(typeAtacher) {
    let types = typeAtacher.split(",");
    types = types.map(t => t.trim().toLowerCase());
    if (types.length === 1) {
        types.push("");
    }
    return [CorrectionAurtographique(types[0]), CorrectionAurtographique(types[1])];
}
function CorrectionAurtographique(mot, num=0) {
    if (mot == "") return "";
    let listeMots = ["acier", "combat", "dragon", "eau", "électrique", "fée", "feu", "glace", "inconnu", "insecte", "normal", "obscur", "plante", "poison", "psy", "roche", "sol", "spectre", "ténèbres", "vol"];
    if (num == 1) listeMots = listeDeTousLesNoms;

    mot = mot.trim().toLowerCase();

    // Fonction de distance de Levenshtein
    function levenshtein(a, b) {
        const matrix = [];
        for (let i = 0; i <= b.length; i++) {
            matrix[i] = [i];
        }
        for (let j = 0; j <= a.length; j++) {
            matrix[0][j] = j;
        }
        for (let i = 1; i <= b.length; i++) {
            for (let j = 1; j <= a.length; j++) {
                if (b.charAt(i - 1) === a.charAt(j - 1)) {
                    matrix[i][j] = matrix[i - 1][j - 1];
                } else {
                    matrix[i][j] = Math.min(
                        matrix[i - 1][j - 1] + 1, // remplacement
                        matrix[i][j - 1] + 1,     // insertion
                        matrix[i - 1][j] + 1      // suppression
                    );
                }
            }
        }
        return matrix[b.length][a.length];
    }

    // Trouve le mot avec la plus petite distance
    let motProche = listeMots[0];
    let distanceMin = levenshtein(mot, motProche);
    for (let i = 1; i < listeMots.length; i++) {
        let dist = levenshtein(mot, listeMots[i]);
        if (dist < distanceMin) {
            distanceMin = dist;
            motProche = listeMots[i];
            tempsI = i;
        }
    }

    return motProche;
}
function Search(num) {
    if (num == 0) {
        ID = parseInt(document.getElementById('Numéro choisie').value);
    }
    else if (num == 1) {
        let nomCherché = document.getElementById('Nom chercher').value;
        let nomTrouvé = CorrectionAurtographique(nomCherché, 1);
        ID = tempsI + 1; // tempsI est défini dans CorrectionAurtographique()
    }
    Suivant(0);
}

function PlusPetitePréEvolution(){
    let ici = ID;
    let stop = false;
    while (stop==false){
        stop = true;
        for (let i = 0; i < évolution.length; i++) {
            if (évolution[i][1] == ici){
                ici = évolution[i][0];
                stop = false;
            }
        }
    }
    return ici;
}

function TrouverConditionEvolution(numéro){//le numéro est celui de l'évoluer
    for (let i = 0; i < évolution.length; i++) {
        if (évolution[i][1] == numéro){
            return évolution[i][2];
        }
    }
    return "";
}

function ConstruireFamilleComplet(premier) {
    let famille = [];
    let visités = new Set();

    function explorer(id) {
        if (visités.has(id)) return;
        visités.add(id);
        famille.push(id);

        for (let evo of évolution) {
            if (evo[0] === id) {
                explorer(evo[1]); // explore chaque évolution possible
            }
        }
    }

    explorer(premier);
    return famille;
}
function ConstruireArbreEvolution(racine) {
    let arbre = [];
    let niveauActuel = [racine];

    while (niveauActuel.length > 0) {
        // Ajout du niveau actuel à l'arbre
        arbre.push(niveauActuel);

        // Récupérer les évolutions possibles depuis ce niveau
        let prochainNiveau = [];
        for (let id of niveauActuel) {
            for (let evo of évolution) {
                if (evo[0] === id) {
                    prochainNiveau.push({ id: evo[1], condition: evo[2] });
                }
            }
        }

        // Organiser les conditions et ids séparément
        if (prochainNiveau.length > 0) {
            arbre.push(prochainNiveau.map(e => e.condition)); // ligne des conditions
            niveauActuel = prochainNiveau.map(e => e.id);     // ligne des nouvelles formes
        } else {
            niveauActuel = [];
        }
    }
    return arbre;
}
function PlacerLesEvolution() {
    table.innerHTML = "";
    let racine = PlusPetitePréEvolution(ID);
    let arbre = ConstruireArbreEvolution(racine);

    for (let i = 0; i < arbre.length; i++) {
        if (typeof arbre[i][0] === "string") {
            // Ligne de conditions
            //AjouterUneLigneTexte(arbre[i]);
        } else {
            // Ligne de créatures
            AjouterUneLigneMalomon(arbre[i]);
        }
    }
}

function AjouterUneLigneMalomon(mots){//mots est une suite de nombre dans un tableau;
    let trImages = document.createElement("tr");
    for (let i = 0; i < mots.length; i++) {
        let td = document.createElement("td");
        td.style.textAlign = "center";
        let conditionEvolution = TrouverConditionEvolution(mots[i]);
        if (conditionEvolution != ""){
            let texteCondition = document.createElement("div");
            texteCondition.textContent = conditionEvolution;
            td.append(texteCondition);
            let barre = document.createElement("hr");
            td.append(barre);
        }

        let img = document.createElement("img");
        img.src = mesDictionnaire[mots[i]-1].image;
        ErreurImage(img, mesDictionnaire[mots[i]-1]["nom"], mesDictionnaire[mots[i]-1]["ID"]);
        img.style.height = "64px";

        let nom = document.createElement("div");
        nom.textContent = mesDictionnaire[mots[i]-1].nom;

        td.appendChild(img);
        td.appendChild(nom);
        trImages.appendChild(td);
    }
    table.appendChild(trImages);
}

function AjouterUneLigneTexte(mots){//mots est un tableau de chaine de caractère
    for (let i = 0; i < mots.length; i++) {
        let trTexte = document.createElement("tr");
        let tdTexte = document.createElement("td");
        tdTexte.style.textAlign = "center";
        let texte = document.createElement("div");
        texte.textContent = mots[i];
        tdTexte.append(texte);
        trTexte.appendChild(tdTexte);
        table.appendChild(trTexte);
    }
}

document.querySelectorAll("img").forEach(img => {
    img.addEventListener("click", () => {
        ajouterEffetRebond(img);
    });
});
function ajouterEffetRebond(element) {
    if (!element) return;
    element.classList.remove("bounce"); // pour pouvoir relancer l'anim
    void element.offsetWidth;           // force un "reflow" du navigateur
    element.classList.add("bounce");
}