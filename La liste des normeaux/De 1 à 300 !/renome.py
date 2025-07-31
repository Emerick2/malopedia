import os
import shutil
import json
import csv
from pathlib import Path
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import re


POKEMON_TYPES = [
    "Normal", "Feu", "Eau", "Plante", "Électrik", "Glace", "Combat", "Poison",
    "Sol", "Vol", "Psy", "Insecte", "Roche", "Spectre", "Dragon", "Ténèbres",
    "Acier", "Fée"
]

positionDeMonJSON = "C:\\Users\\compteadmin\\Desktop\\malo\\exercice restrain\\descriptions.json"

def JamaisRenomé(nom):
    nombre = ["0","1","2","3","4","5","6","7","8","9"]
    n=""
    réussie = True
    for i in nom :
        if i in nombre and réussie == True:
            n+=i
        else:
            réussie=False
    return [réussie, n]


def Renomé(nomX,extension):
    dictionnaire = {
    "iDFixe":"",
    "iDChangable":"",
    "tipe1":"",
    "tipe2":"",
    "description":"",
    "nom":""}

    v=JamaisRenomé(nomX)
    if v[1]==True:
        dictionnaire["iDFixe"] = v[1]
        dictionnaire["iDChangable"] = v[1]
    else :
        étape = 1
        contenu = ""
        for i in nomX :
            if (étape==1 and i == "%"):
                dictionnaire["iDChangable"] = contenu
                contenu = ""
                étape = 2
            elif (étape == 2 and i == "["):
                dictionnaire["iDFixe"] = contenu
                contenu = ""
                étape = 3
            elif (étape == 3 and i==","):
                dictionnaire["tipe1"] = contenu
                contenu = ""
                étape = 4
            elif (étape == 4 and i == "]"):
                dictionnaire["tipe2"] = contenu
                contenu = ""
                étape = 5
            elif (étape==5 and i=="!"):
                dictionnaire["nom"] = contenu
                contenu = ""
                étape = 6
            elif (étape != 6):
                contenu+=i
        if (dictionnaire["iDFixe"] == "" and v[1] != ""):
            dictionnaire["iDFixe"] = v[1]
            dictionnaire["iDChangable"] = v[1]
        dictionnaire["description"] = LireJSON(dictionnaire["iDFixe"])
    return dictionnaire


def EcrireJSON(clef, valeur):
    global positionDeMonJSON
    desc_path = Path(positionDeMonJSON)
    if desc_path.exists():
        with open(desc_path, 'r', encoding='utf-8') as f:
            données = json.load(f)
        
        données[clef] = valeur

        with open(desc_path, 'w', encoding='utf-8') as f:
            json.dump(données, f, indent=4, ensure_ascii=False)

def LireJSON(clef):
    global positionDeMonJSON
    desc_path = Path(positionDeMonJSON)
    if desc_path.exists():
        with open(desc_path, 'r', encoding='utf-8') as f:
            données = json.load(f)
        return données.get(clef, "")
    return ""

def retirer_tabulations(tableau):
    return [valeur.replace('\t', '') for valeur in tableau]


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Malomon Manager")
        self.geometry("700x400")
        self.ChoisireDossier()
        self.CreateWidgets()
        self.index = 0
        #self.UtiliserDonnéCSV()

    def UtiliserDonnéCSV(self):
        
        listeNom = [
            "	Sourimide	",
            "	Ratonné	",
            "	Lérotivé	",
            "	Hupplague	",
            "	Canarigolo	",
            "	Rapascié	",
            "	Rézouga	",
            "	Guppifi	",
            "	Dauphertz	",
            "	Amplégnée	",
            "	Bagallen	",
            "	Auberswing	",
            "	Pistilonde	",
            "	Frono	",
            "	Madonde	",
            "	Flenouille	",
            "	Gretus	",
            "	Grisouille	",
            "	Pollenouille	",
            "	Racinouille	",
            "	Bistondu	",
            "	Bostaurus	",
            "	Somaloucouton	",
            "	Rat-Porc	",
            "	Salmiri	",
            "	Pyroups	",
            "	Gendhocore	",
            "	Plivernichard	",
            "	Tapicvert	",
            "	Bérace	",
            "	Chapace	",
            "	Laperose	",
            "	Laperine	",
            "	Liévroile	",
            "	Moucouton	",
            "	???	",
            "	Ferné	",
            "	Stolnneau	",
            "	Gigonneau	",
            "	Aragliffe	",
            "	Moustagliffe	",
            "	Totierre	",
            "	Poulaçon	",
            "	Paonlet	",
            "	Ouilletruche	",
            "	Renfotruche	",
            "	Doubletruche	",
            "	Rigelure	",
            "	Proustache	",
            "	Chérochette	",
            "	Titappébrique	",
            "	Appébrique	",
            "	Végébrique	",
            "	Aquabrique	",
            "	Grosappébrique	",
            "	Larvuce	",
            "	Puscle	",
            "	Puçagile	",
            "	Bébouton	",
            "	Cammlherb ♂	",
            "	Cammlherb ♀	",
            "	Serable	",
            "	Limasable	",
            "	Roclaclape	",
            "	Domectus	",
            "	Cactouaf	",
            "	Repentriste	",
            "	Templeur	",
            "	Servant	",
            "	Lochtin	",
            "	Élantorche	",
            "	Élamptorche	",
            "	Losome	",
            "	Fanchet	",
            "	Flix	",
            "	Ductar	",
            "	Chanzon	",
            "	Canekton	",
            "	Canactrik	",
            "	Coruses	",
            "	Lamentuse	",
            "	Escalâme	",
            "	Vanivanivane	",
            "	Globoulet	",
            "	Blobain	",
            "	Mainguille	",
            "	Alguignon	",
            "	Bigalguignon	",
            "	Gigalguignon	",
            "	Grogarchon	",
            "	Cornilon	",
            "	Palmouée	",
            "	Bloinbloin	",
            "	Haben	",
            "	Racouchtaï	",
            "	Turbuglu	",
            "	Pistépholle	",
            "	Tifibtech	",
            "	Gronébrilateur	",
            "	Palmuno	",
            "	Tripleam	",
            "	Dieshirique	",
            "	Multibrique	",
            "	Ponvolant	",
            "	Cochainu	",
            "	Komiglier	",
            "	Komalion	",
            "	Corsouette	",
            "	Mateloquette	",
            "	Corsouet	",
            "	Mateloquet	",
            "	Mouvhante	",
            "	Bouorte	",
            "	Chausovol	",
            "	Turgouille	",
            "	Touquin	",
            "	Fourmy	",
            "	Araigner	",
            "	Grenwille	",
            "	Taupor	",
            "	Chaudronor	",
            "	Hériluche	",
            "	Scootardi	",
            "	Voicifé	",
            "	Fullaby	",
            "	Wallombre	",
            "	Cristomb	",
            "	Vipombre	",
            "	Ombruche	",
            "	Ptilmier	",
            "	Coupalmier	",
            "	Troutrouille	",
            "	Citorcier	",
            "	Arbagaah	",
            "	Patate	",
            "	Papilloteau	",
            "	Babarillon	",
            "	Verché	",
            "	Totenille	",
            "	Soufflenille	",
            "	Ailtton	",
            "	Arainele	",
            "	Trapierrêve	",
            "	Tigeoulin	",
            "	Dodugon	",
            "	Bânârî	",
            "	Flâcârî	",
            "	Wombster	",
            "	Gorégétation	",
            "	Citraou	",
            "	Fourmiquet	",
            "	Bébochère	",
            "	Phacolère	",
            "	Rembouruffle	",
            "	Flamair	",
            "	Diaspectament	",
            "	Brûchoiragla	",
            "	Glachoire	",
            "	Combali	",
            "	Dragali	",
            "	Capicool	",
            "	Anncro	",
            "	Antiquomme	",
            "	Monobi	",
            "	Fleunouille obscur	",
            "	Laperobel	",
            "	Lihontèvre	",
            "	Blorkblork	",
            "	Canactracté	",
            "	Colèréktrik	",
            "	Piratate	",
            "	Kapïkou	",
            "	Euthimy	",
            "	Ébeniffon	",
            "	Crocacraco	",
            "	Solailer	",
            "	???	",
            "	Cacouet	",
            "	Léotus	",
            "	???	",
            "	???	",
            "	???	",
            "	???	",
            "	???	",
            "	???	",
            "	Dicaille	",
            "	patatesombre	",
            "	marteuille	",
            "	Luminaire	",
            "	Vitrilô	",
            "	Flâmitlô	",
            "	Extrâvillô	",
            "	Gourex	",
            "	Goéroo	",
            "	Fignée	",
            "	Fignée forme voyageur	",
            "	Carapigue	",
            "	Figuèpe	",
            "	Afrask	",
            "	Patate étourdie	",
            "	Coquinuit	",
            "	Cruchard	",
            "	Grelouphore	",
            "	Chatodeau	",
            "	Tortulipe	",
            "	Timilipe	",
            "	Dragalipe	",
            "	Dédé	",
            "	Morpiâme	",
            "	Feuneille	",
            "	Topfer	",
            "	Chaudrofer	",
            "	???	",
            "	???	",
            "	???	",
            "	???	",
            "	???	",
            "	???	",
            "	???	",
            "	???	",
            "	???	",
            "	???	",
            "	???	",
            "	???	",
            "	???	",
            "	???	",
            "	Parachusette	",
            "	???	",
            "	???	"
                    ]
        listeType = [
            "	plante	",
            "	plante	",
            "	plante, poison	",
            "	feu	",
            "	feu	",
            "	feu, vol	",
            "	eau	",
            "	eau	",
            "	eau, psy	",
            "	plante	",
            "	plante, poison	",
            "	plante, poison	",
            "	plante	",
            "	plante, fée	",
            "	plante, fée	",
            "	plante, normal	",
            "	plante	",
            "	plante, ténèbres	",
            "	plante, fée	",
            "	plante, sol	",
            "	ténèbre	",
            "	normal 	",
            "	normal, fée	",
            "	Sol	",
            "	plante et psy	",
            "	insecte, normal	",
            "	insecte, normal	",
            "	vol	",
            "	vol	",
            "	normal	",
            "	normal	",
            "	normal	",
            "	fée	",
            "	fée	",
            "	insecte, fée	",
            "		",
            "	acier, insecte	",
            "	roche	",
            "	roche	",
            "	roche, ténèbres	",
            "	roche, plante	",
            "	roche	",
            "	roche, glace	",
            "	roche glace	",
            "	combat	",
            "	combat	",
            "	combat, acier	",
            "	roche	",
            "	roche, électrik	",
            "	roche, électrik	",
            "	roche	",
            "	roche	",
            "	roche, plante	",
            "	roche, eau	",
            "	roche	",
            "	insecte	",
            "	sol, insecte	",
            "	vol, insecte	",
            "	plante	",
            "	sol, plante	",
            "	sol, plante	",
            "	sol	",
            "	sol, psy	",
            "	Sol	",
            "	sol	",
            "	sol, plante	",
            "	spectre	",
            "	spectre, sol	",
            "	normal	",
            "	normal	",
            "	feu	",
            "	électrik	",
            "	acier, eau	",
            "	acier, eau	",
            "	eau, poison	",
            "	eau, poison	",
            "	eau, poison	",
            "	électrik	",
            "	électrik	",
            "	poison, eau	",
            "	poison, eau	",
            "	plante, dragon	",
            "	eau fée	",
            "	combat	",
            "	combat	",
            "	combat, eau	",
            "	eau	",
            "	eau	",
            "	eau, dragon	",
            "	plante	",
            "	plante, vol	",
            "	plante, eau	",
            "	eau	",
            "	psy	",
            "	insecte, feu	",
            "	insecte, feu	",
            "	Insecte / Feu	",
            "	Électrik	",
            "	Électrik	",
            "	plante	",
            "	plante	",
            "	sol	",
            "	sol	",
            "	sol, vol	",
            "	feu	",
            "	feu	",
            "	feu	",
            "	eau	",
            "	eau	",
            "	eau	",
            "	eau	",
            "	acier, spectre	",
            "	plante, electrik	",
            "	feu	",
            "	eau	",
            "	normal	",
            "	normal	",
            "	normal	",
            "	normal	",
            "	acier	",
            "	acier	",
            "	normal	",
            "	acier, fée	",
            "	acier, fée	",
            "	combat	",
            "	combat, ténèbre	",
            "	spectre	",
            "	spectre, ténèbre	",
            "	spectre, ténèbre	",
            "	plante	",
            "	plante	",
            "	plante	",
            "	plante, psy	",
            "	plante, psy	",
            "	sol	",
            "	acier, insecte	",
            "	acier, insecte	",
            "	sol	",
            "	sol, poison	",
            "	sol, poison	",
            "	insecte, psy	",
            "	insecte, psy	",
            "	insecte, psy	",
            "	dragon	",
            "	dragon	",
            "	electrik	",
            "	feu	",
            "	norma, vol	",
            "	plante	",
            "	plante, psy	",
            "	insecte, feu	",
            "	glace	",
            "	combat glace	",
            "	combat glace	",
            "	vol feu	",
            "	spectre	",
            "	eau feu	",
            "	eau feu	",
            "	combat	",
            "	dragon	",
            "	normal poison	",
            "	dragon	",
            "	plante eau	",
            "	psy	",
            "	ténèbre plante	",
            "	ténèbre normal	",
            "	ténèbre normal	",
            "	ténèbre eau	",
            "	ténèbre électrique	",
            "	ténèbre électrique	",
            "	dragon fée	",
            "	spectre combat	",
            "	vol feu	",
            "	vol fée	",
            "	vol sol	",
            "	psy vol	",
            "		",
            "	sol acier	",
            "	sol acier	",
            "	combat insecte	",
            "	roche acier	",
            "	glace acier	",
            "	sol psy	",
            "	plante fée	",
            "	feu dragon	",
            "	eau dragon	",
            "	sol spectre	",
            "	combat électrique	",
            "	poison électrique	",
            "	dragon	",
            "	feu dragon	",
            "	feu dragon	",
            "	eau vol	",
            "	eau vol	",
            "	insecte	",
            "	insecte	",
            "	insecte	",
            "	insecte vol	",
            "	insecte ténèbre	",
            "	sol psy	",
            "	glace, poison	",
            "	eau	",
            "	eau	",
            "	eau, sol	",
            "	plante	",
            "	plante	",
            "	plante, dragon	",
            "	spectre	",
            "	spectre	",
            "	feu	",
            "	Acier	",
            "	acier	",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "	électrique	",
            "		",
            "		"]
        listeDescription = [      
            "	Sourimide est très craintif, il vit en groupe et il mange de la terre. C'est également le starter de type plante du pays de Malo-Malo !	",
            "	Curieux de tout, il est intelligent et vit en groupe. Son esprit d'équipe le pousse à toujours prioriser les siens plutôt que lui-même. 	",
            "	Véritable meneur dans l'âme, il est charismatique et bienveillant, capable de tout pour protéger son clan comme son territoire. Il n'est pas rare qu'il défende dans ses feuillages de petits malomons pour lesquels il s'est épris d'affection.	",
            "	C'est un passionné d'humour, tout particulièrement du comique de répétition. En grandissant, il prendra confiance en lui pour tenter ses propres blagues s'il grandit dans une atmosphère de confiance.	",
            "	Très sociable, il a à coeur de s'attacher à un groupe d'amis dont il ne se séparera plus. Souvent bon joueur et bon public, c'est un camarade sur qui l'on peut compter. 	",
            "	Grand prédateur nichant sur les hauteurs des monts enneigés de Flocoland, c'est de la puissance des flammes animant ses trois yeux qu'il tire sa clairvoyance. Oui, trois yeux, vous avez bien lu : la sphère au centre de son torse en est un lui aussi.	",
            "	La plupart des scientifiques s'accordent à lui décerner le prix du malomon le plus facile à vivre, toutes catégories confondues ! Presque incapable de se déplacer seul, il n'en a de toute façon pas l'utilité ni l'envie. Il peut tout-à-fait survivre une année sans boire ni manger. Il est toujours de bonne humeur, n'ouvre jamais la bouche, ne tente jamais rien. Il est là. C'est tout. Et il est content. ",
            "Atout non négligeable, il émet sans discontinuité un réseau internet par sa bosse. Il n'est donc pas rare d'en voir de posés dans des cafés ou lieux publics, offrant un réseau gratuit pour toute la clientèle.	",
            "	Si sa pré-évolution vivait aussi bien sur terre qu'en mer, guppifi préférera nettement ce second environnement où ses nouvelles nageoires en feront un bon nageur. Puisqu'il n'a pas de branchies, il use de ses capacités psychiques contenues dans son cortexe frontal pour maintenir une bulle d'air autour de sa tête.	",
            "	Cette force de la nature est d'une grande intelligence. Il capte et analyse chacun des mouvements du milieu aquatique dans lequel il évolue, à plusieurs kilomètres à la ronde. Il est très apprécié des équipes de secours en mer et de la marine pour son tempérament calme et son extrême précision. 	",
            "	Présent dans tous les coins de verdure de Malo-Malo, et dans de nombreux espaces verdoyants de Crocland, il a la particularité d'émettre ses sons par son unique œil.	",
            "	Il prend plaisir à frapper de coups de poing tout ce qui l'entoure, diffusant par la même occasion des pollens. 	",
            "	Il émet par ses avant-bras des mélodies en continu. Le soleil lui est vital et il flétrie à vue d'œil sans lui.	",
            "	Il s'agit du pendant féminin de l'Amplégnée. Plus discrète, elle prend soin de la tige de sa tête et sort rarement le jour. 	",
            "	Il faut un mois au fruit au-dessus de sa tête pour pousser. Quand il est mûr, il tombe et c'est un amplégnée ou un pistilonde qui naît !	",
            "	Elle dirige d'une main de fer son nid. Gare à qui osera s'en prendre à une frono sous ses yeux !	",
            "	Très sympathiques, les fleunouilles gambadent naïvement entre les nénuphars et les champs de fleurs. 	",
            "	Les fleunouilles appréciant particulièrement les nénuphars ont fini par en emprunter des propriétés, lorsqu'ils évoluent en gretus.	",
            "	Cette évolution lui permet d'être mieux adapté aux tapis de feuilles et aux mares de boue dans lesquelles il se dissimule. Sa peau moite sécrète une toxine très utilisée dans des produits d'hygiène populaires.	",
            "	Les pellicules de son crâne sont un condensé de pollens aux parfums enivrants, qu'il répand où qu'il passe. C'est la bête noire des pauvres dresseurs allergiques.	",
            "	Pour se nourrir, il pose sa tête au sol et s'alimente des nutriments que ses racines crâniennes puisent de la terre. 	",
            "	Sa laine tombe naturellement tout au long de l'année, alors il la stocke avec sa queue. Dès qu'il en a besoin, il a ainsi de la laine à portée de patte !	",
            "	En dépit de ses très longues cornes, c'est un éternel pacifiste. Traditionnellement, les villages qui l'ont domestiqué l'élevaient pour son lait, ainsi que pour ses excréments à partir desquels sont batties encore aujourd'hui des maisons. 	",
            "	Cousin de Moucouton, le Somaloucouton est cependant 10x plus gros, atteignant les 1m50 de hauteur environ. Il est sans cesse en déplacement, sur ses multiples pattes, roulant comme un ballon ! Pour se stabiliser, il lève ses multiples pattes et tient sur son solide front uniquement. Mais... Il ne voit plus rien dès lors. 	",
            "	Il n'aime pas le fromage, ce n'est pas un rat. Il n'aime pas la boue, ce n'est pas un porc. Pourquoi les gens se trompent tout le temps ?! Ce n'est pas un rat, ce n'est pas un porc, alors où est le rapport ??!	",
            "	Il aime se balader de branche en branche avec sa double queux pour regarder les activités des autres malomon peuplant sa région !	",
            "	Curieux du monde qui l'entoure, il passe tout son temps libre à en observer le fonctionnement.	",
            "	Intimement persuadé d'avoir saisi le fonctionnement de notre monde, il s'acharne à y faire respecter des règles qu'il a lui même érigé. 	",
            "	Il sont frêles et encore aveugles, totalement dépendants de leurs parents qui enchaînent les allers retours afin de les nourrir de Larvuces frais.	",
            "	Un recensement récent a révélé qu'il s'agissait de l'oiseau le plus répandu de Malo Malo. Il creuse la terre ou le sable à la recherche de larvuces frais, quand ceux-ci ne sautent pas directement dans son bec. 	",
            "	Si certains amateurs prêtent à sa bave des vertus thérapeutiques, elle est en réalité communément admise comme complètement banale.	",
            "	Il fut un temps où porter ce pokémon sur sa tête était le signe de son appartenance à une classe supérieure. La pratique s'est par la suite démocratisée, si bien qu'elle est devenue l'un des emblèmes de la tradition malo-malouine.	",
            "	Ce petit mammifère creuse ses terriers dans les sols meubles, provoquant bien souvent la colère d'agriculteurs. 	",
            "	Précautionneux, il prend soin de sa fourrure rose à longueur de journée. Sa grace naturelle en fait un partenaire de choix pour les concours pokémon. 	",
            "	Atteignant très rarement ce stade d'évolution à l'état sauvage, c'est par un entraînement acrobatique et physique intense qu'il a su s'élever à ce niveau de grace couplée à la force d'une véritable danseuse étoile.	",
            "	Ne dépassant pas les 15 cm, cette pelote de laine volante se nourrit de moutons de poussière exclusivement. Bien qu'il soit inoffensif, se retrouver pris dans une nuée de plusieurs centaines ou milliers de ce malomon est très impressionnant.	",
            "		",
            "	Il y a peu de temps encore, les biologistes le classaient dans une famille à part avant de s'appercevoir qu'il était lui-même issu d'un malomon. ",
            "Solitaire, renfermé, peu émotif et résistant, il a tendance à vivre en bande sous les troncs d'arbres morts et dans l'humidité. ",
            "	Est-ce un tonneau ? Non, c'est un stolnneau ! Il se bat avec son unique membre de pierre, qu'il peut étendre jusqu'à 10 mètres autour de lui. 	",
            "	Ce pokémon troglodyte vit dans les sous-sols des îles de Malo Malo. Joueur, il aime se faire passer pour une simple stalagmite et effrayer les pokémons alentours.	",
            "	Les aragliffes vivent dans les cavités les plus profondes de la terre, souvent proches des poches volcaniques. Terrifiants, imprévisibles et très puissants, ils sont très difficiles à domestiquer, même pour un dresseur aguerri.	",
            "	Le Moustagliffe est un pokémon extrêmement rare à l'état sauvage, puisque les gigonneaux ne sortent normalement jamais de leurs grottes. S'étant adapté à son nouveau milieu de vie, il protège les plus petits pokémons de sa forêt qu'il considère comme ses enfants. Pour les rassurer, ou quand une situation dégénère, il remue en rythme les tonneaux aux extrémités de ses bras, à la manières de hochets ou de maracasses.	",
            "	Ce pokémon ne mange pas, ne boit pas, et ne bouge pas. Souvent confondu par les badauds avec une simple pierre, il s'agit en fait d'un œuf qui n'attend qu'un grand froid pour se développer.	",
            "	Présent dans les zones de grand froid, ce malomon peu commode absorbe la neige qui l'entoure d'où il puise son énergie. 	",
            "	Fier et belliqueux, ce malomon mène la vie dure à ses voisins. Il pond de très nombreux Totierre tout au long de sa vie, sur les chemins qu'il parcourt.	",
            "	Il pique et, à chacun de ses coups, il fait dire 'ouille' à ses adversaires.	",
            "	Il s'est renforcé et chacun de ses coups font dire 'OUILLE', je devrais aussi me renforcer à ses adversaires !	",
            "	Il peut attaquer deux personnes à la fois avec ses deux piques.	",
            "	Joyeux et insouciant, les rigelures sont très curieux du monde qui les entoure.	",
            "	Se voulant distingué et philosophant de sa place dans le monde, ce pokémon a appris à être calme et apprécie la solitude.	",
            "	Ce pokémon est capable d'absorber une très grande quantité de foudre ! Ses poils sont remplis d'électricité, qui électrocuteront légèrement quiconque les touchera. 	",
            "	Ce pokémon ressemblant à une brique de construction infeste les cavités de roche, les gouffres, et parfois même les grottes. Tout au long de la journée, il se nourrit de pierre qu'il emmagasine pour grossir et se renforcer. 	",
            "	La plupart des gouffres de Malo-Malo et Crocland sont dûs à son appétit vorace. Avec ses pattes malhabiles, il peut maintenant se déplacer pour trouver une pierre plus nourrissante.	",
            "	Il s'agit d'un titapébtique ayant ingurgité trop de végétaux, qui ont fini par modifier son métabolisme. Il ne mange presque plus, et sa croissance est terminée.	",
            "	Il s'agit d'un titapébtique ayant ingurgité trop de végétaux aquatiques, qui ont fini par modifier son métabolisme. Il ne mange presque plus, et sa croissance est terminée.	",
            "	Glouton invétéré, sa mâchoire peut tout broyer. Il s'agit d'un dangereux prédateur pour tout malomon du type roche, comme les gravalanch ou les gigonneaux. 	",
            "	Certaines plages sont fuites des touristes, tant le sable est infesté de ce petit malomon qui s'y niche à quelques centimètres de profondeur seulement. La plupart finiront malheureusement dans le bec d'un malomon oiseau.	",
            "	Les rares larvuces à avoir atteint l'âge adulte évolueront en puscle si c'est en creusant plus profondément qu'ils sont parvenus à se nourrir, développant ainsi leur musculature et leur solide carapace. 	",
            "	Les rares larvuces à avoir atteint l'âge adulte évolueront en puçagile si c'est en sortant de terre et en apprenant à bondir qu'ils sont parvenus à se nourrir, développant ainsi leurs jambes arrières et leur agilité.	",
            "	Il passe le plus clair de son temps à dormir. Il s'envole au gré du vent, indépendamment de sa volonté, à travers les zones désertiques qu'il habite.	",
            "	En croiser un dans le désert est synonyme de bon présage, car ce pokémon vit près des oasis et des points d'eau. 	",
            "	En croiser un dans le désert est synonyme de bon présage, car ce pokémon vit près des oasis et des points d'eau. 	",
            "	Synonyme de mauvais présage, ce pokémon rare, solitaire et agressif semble avoir accumulé une partie de la rancoeur d'une ancienne vie qu'il extériorise par le sable qu'il projette depuis la pointe du cône qu'il a sur la tête. 	",
            "	Très rare, ce pokémon est pourtant recherché par de nombreux explorateurs avides de richesses qui ne le chassent que pour l'énorme rubis qui pousse à l'extrémité de sa queue.	",
            "	Il passe ses journées les bras grands ouverts, à attendre qu'une proie s'y engouffre pour refermer sur elle le piège. 	",
            "	Ce malomon partage le même ancêtre commun que Cacouet mais, contrairement à ce dernier, Domectus a été domestiqué par l'homme de qui il est désormais très proche. Bien qu'un peu turbulent, c'est un compagnon idéal pour les enfants.	",
            "	Souvent utilisé comme malomon garde pour sa grande obéissance et sa fidélité sans faille, il a généralement un état d'esprit de protecteur très développé. 	",
            "	Ses yeux rubis reflètent les remords de ceux qu'ils croisent. Si vous le regardez un peu trop longtemps, nul doute que vous vous perdrez vous aussi dans vos regrets enfouis les plus troublants.	",
            "	Il est à l'origine de nombreuses tempêtes de sable, dans le désert. On entend les gémissements lugubres de ce malomon à travers ses tempêtes. 	",
            "	Doux comme un doudou, jovial comme une peluche et réconfortant comme un ami, ce petit malomon tout rond et naïf est presque inoffensif.	",
            "	Il est plus habile de ses mains de bois qu'il a sur sa tête plutôt que de ses pattes. Souple et à l'affût, il est curieux du monde qui l'entoure.	",
            "	Maniant désormais le feu, il éclaire et protège ainsi tout son troupeau. Il est généralement sage, précautionneux, protecteur.	",
            "	Son évolution est dûe à l'intervention de l'Homme qui, en créant l'énorme torche électrique que le pokémon s'est ensuite approprié, a permis à ce dernier de trouver le moyen d'éclairer son troupeau d'une façon différente mais non moins efficace que ses confrères Élantorches.	",
            "	Il pourrait se nourrir des conserves et autres déchets polluant les fonds marins, mais préfère s'attaquer au récif brut. 	",
            "	Sa vitesse de pointe peut atteindre les 150 km/h ! Il éprouve cependant de grandes difficultés à tourner sur un côté, et est bien incapable de se retourner sur lui-même. 	",
            "	Sa joie de vivre et son optimisme n'ont d'égales que ses capacités de chanteur infatigable ! Il est peu habile si bien dans l'eau que sur terre. 	",
            "	Sa nouvelle voix nasillarde ne l'empêche pas de continuer ses chansons. Il ne se préoccupe pas de ses voisins pokémon tant que ceux ci ne viennent pas le déranger.	",
            "	Il s'approprie un lac, cours d'eau ou lagune, et intimide tout adversaire grâce à la puissance de ses cordes vocales.	",
            "	Toujours collés entre frères et sœurs, ils s'électrocutent sans cesse entre-eux par erreur. 	",
            "	Généralement bougon, il tente de régler tous ses problèmes par une simple dégage électrique.	",
            "	Bien qu'il s'agisse d'un unique malomon, de nouvelles têtes ayant leur propre cerveau indépendant en poussent sans cesse. Si l'une d'elle est séparée du corps commun, elle continue de pousser et devient un malomon à part entière. 	",
            "	Il s'est libéré de son rocher et nage librement dans les profondeurs des mers et océans.	",
            "	Il escalade chaque jour les plus grand chose qu'il voie (que ce soit des arbre, grate ciel, montagne...) Durent sa monter il renforce ces plume d'une aura très puisante qui, une fois toute en haut, il partagera a toute les malomon dès alentoure la force qu'il à accumuler à l'aide d'un grand champ mélodieux.	",
            "		",
            "	Il est sans cesse à la recherche de matériaux ou malomon compactes à pulvériser. En ville, la présence de ce téméraire serait une véritable calamité ! 	",
            "	Si certains le trouvent très moche, c'est en revanche un compagnon idéal pour les enfants.	",
            "	Quand il repère un humain ou pokémon, il prend plaisir à lui foncer dans le ventre à toute vitesse ! 	",
            "	Son unique espoir de survie face à ses nombreux prédateurs est de ne jamais quitter les zones protégées par le gigalguignon qui lui a donné la vie.	",
            "	Les algues qui se développent sur son corps sont utilisées dans de nombreuses recettes de yaourts.	",
            "	Enraciné en profondeur, il couverture sous son immense chapeau des milliers d'Alguignons qu'il protège par ses poisons.	",
            "		",
            "		",
            "	Il vogue sur les eaux au gré des courants. Quand il est en danger, il frappe vivement la surface avec sa feuille pour sd propulser et prendre la fuite.	",
            "	Fonceur et bêta, mais avec un bon fond. Il peut se prendre d'émerveillement pour quelqu'un et l'imiter comme un disciple.	",
            "	Incroyablement possessif, il refuse de lâcher ce qu'il a commencé à attraper.	",
            "	Envahissant, sale, étonnamment résistant, sa présence s'accompagne souvent d'odeurs nauséabondes.	",
            "	Toujours aussi sale et envahissant, il a pris en volume et est maintenant bien plus difficile à faire fuire ! Ils s'agglutinent près des poubelles, en ville. 	",
            "	Seuls les Turbuglus ruraux atteignent parfois ce stade d'évolution. Ils diciment les champs qu'ils traversent.	",
            "	Domestiqué par l'homme, il n'existe presque plus à l'état sauvage. Sa maîtrise précise du voltage de ses attaques en fait un allié utile dans de nombreux domaines.	",
            "	Ses décharges maîtrisées peuvent permettre de relancer le coeur d'un humain ou malomon en arrêt cardiaque. C'est le compagnon privilégié des pompiers et secouristes de Malo Malo.	",
            "	il vive souvent a spadaland ces un malomon très répendu dans les familles 	",
            "	ce malomon est assez rare, il est souvent visibles dans les endroits important de la ville 	",
            "	il a été très utilisé pour la construction à saint dustriel	",
            "	il protège les habitants en formant un épais large et au mur devant eu	",
            "	il permet de placer des ponts n'importe où et son espèce a sauvé beaucoup d'habitants pendant une certaine période de l'histoire 	",
            "	Considéré sacré dans les lointaines contrées dont il est originaire, il a été importé à Crocland et Malo Malo par des navigateurs marchands il y a de ça bientôt 500 ans.	",
            "	Il s'attache à un lieu représentant de fortes symboliques qu'il respecte et souhaite protéger. Toute sa vie durant, il restera fidèle à ce lieu qu'il ne quittera plus.	",
            "	Maître gardien du lieu qu'il a choisi de protéger, sa noblesse d'âme le pousse à transmettre ses sages convictions à toute personne ou malomon croisant sa route.	",
            "	Compagnon historique du Malo Maloin marin, c'est tout naturellement qu'il est devenu la mascotte du pays de Malo Malo. Leur esprit de camaraderie est une force !	",
            "	Vieux loups de mer sentant les embruns, ils guettent les allés et venus des matelots. Leur couvre chef indique leur grade au sein du bateau. 	",
            "	Compagnon historique du Malo Maloin marin, c'est tout naturellement qu'il est devenu la mascotte du pays de Malo Malo. Leur esprit de camaraderie est une force !	",
            "	Vieux loups de mer sentant les embruns, ils guettent les allés et venus des matelots. Leur couvre chef indique leur grade au sein du bateau. 	",
            "	Maison fantôme par excellence, son existence fut longtemps contestée faute de preuves. Ceux qui y pénètrent n'en ressortent jamais, réincarnés en un malomon qui résidera pour toujours dans le manoir.	",
            "	Il se cale dans les creux rectangulaires et se fait passer pour une porte. Gare à qui en enclenchera la poignée, car elle est électrique !	",
            "		",
            "	Il s'agit d'un serpent d'eau douce, qui s'allonge tout au long de sa vie. Les canalisations de la cité de Karkatson imitent sa forme, si bien que des turgouilles prennent même parfois leur place sans éveiller de soupçons.	",
            "	Race de chien assez basique, il ne possède pas de compétences particulières au combat. Des robes de plus en plus nombreuses existent de son pelage, au gré de croisements faits par les dresseurs.	",
            "	Semblable à une petite main, il est assez inoffensif et fuit le contact de l'Homme.	",
            "	Ils se regroupent au début de l'été à l'occasion d'une fête, pour se partager l'éclosion des oeufs de leur tribu. 	",
            "	Les grenwilles, fourmys et araigners sont génétiquement très proches. De nombreux scientifiques sont à la recherche de traces de leur ancêtre commun le plus proche, jusqu'à présent en vain. 	",
            "	Les métaux rares et pierres précieuses le rendent fou, il passe ses journées à ramper au sol à la recherche de pièces égarées.	",
            "		",
            "	Quand on marche innocemment, il arrive qu'on trébuche en se prenant les pieds dans un hériluche. Quand on ouvre une porte trop fort, il est derrière elle et la fait rebondir. En voiture, si on roule trop vite, il apparaît sous les roues et devient un dos-d'âne très dangereux. Mais, d'où sort-il ?! Il n'était pas là il y a un instant encore ! ...pourtant quoi qu'il arrive, jamais le sourire de son visage ne s'effacera. 	",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "	il fait plus de dégas quand il y a du vent et es inoffensif quand il n'y en a pas 	",
            "		",
            "		",
            "	il a une attaque particulière qui est... le jet de banane enflammé ! il mange chaque jour cinq banane pour sa bonne santé 	",
            "		",
            "		",
            "	il adore faire peur au abitant en se cachant dans les champ de citrouille 	",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "	ces une patate qui ses réfugiés dans une grotte et qui peut désormais voir dans l'obscurité comme dans la journée 	",
            "	il ne voi pas très bien mais adore bricoler des choses inutiles 	",
            "		",
            "		",
            "		",
            "		",
            "		",
            "		",
            "	Né à l'intérieur d'une figue, il y reste et se sert du fruit comme d'un abris en plus d'un garde-manger, ressource de sucre essentielle à son bon développement. ",
            "Quand vous mangerez une figue, ouvrez-là avant de croquer, car ce malomon y niche peut-être !",
            "	Sa courte vie n'a pas dû être simple car, ayant perdu la figue lui servant d'abri et de garde-manger, il est désormais une proie facile et rongé par la faim. Il a sauvé ce qu'il a pu de sa figue disparue et porte ces relicats sur son dos frêle. Pour les protéger, il tente de les dissimuler sous des feuilles ou autres végétaux. 	",
            "	Plus résistant et téméraire, il dispose désormais deux moitiés de figue au niveau de ses avant-bras. Des insectes plus petits que lui sont attirés par l'odeur, piégés par ce malomon devenu prédateur. ",
            "Si besoin ou en fonction de ses envies, il peut aussi choisir de se nourrir directement de cet appât. 	",
            "	Son corps semble produire de la figue. Il vole entre les figuiers où il se nourrit, récupère les figues et en fait un miel rare et réputé. ",
            "De son dard, il pique au prinptemps quelques figues où il dépose en fait ses oeufs qui, après une semaine, verront éclore un figné. 	",
            "	Les difficiles expériences vécues dans sa jeunesse lui ont forgé un caractère fort et persévérant. Rapide, agile, les ciseaux aux extrémités de ses pattes avant coupent comme un rasoir. La feuille couvrant son visage en masque le passage du temps, la couleur flamboyante de cette dernière faisant par ailleurs toute sa fièreté. ",
            "Il effectue une danse pour intimider un adversaire, remercier, ou simplement pour son plaisir. 	"]

        listeNom=retirer_tabulations(listeNom)
        listeType=retirer_tabulations(listeType)
        listeDescription=retirer_tabulations(listeDescription)

        for i in range (0, len(listeNom)):
            numero = str(i + 1)
            image_pathPNG = Path(self.dossier_choisi) / f"{numero}.png"
            image_pathJPG = Path(self.dossier_choisi) / f"{numero}.jpg"
            if image_pathPNG in self.listeImage or image_pathJPG in self.listeImage:
                monNom = listeNom[i]
                maDescription = listeDescription[i]
                mesType = listeType[i]
                types = mesType.split(",")
                monType1 = types[0].strip() if len(types) > 0 else ""
                monType2 = types[1].strip() if len(types) > 1 else ""

                self.SaveData(True, monNom, maDescription, monType1, monType2, i+1)
                
    def LireImage(self, dossier):
        dossier_path = Path(dossier)
        extensions = [".png", ".jpg", ".jpeg"]
        images = [f for f in dossier_path.iterdir() if f.is_file() and f.suffix.lower() in extensions]
        return images
    def ChoisireDossier(self):
        self.dossier_choisi = filedialog.askdirectory(title="Choisissez un dossier")
        self.listeImage = self.LireImage(self.dossier_choisi)
    def CreateWidgets(self):
        self.top_frame = ttk.Frame(self)
        self.top_frame.pack(fill=tk.X)

        self.load_button = ttk.Button(self.top_frame, text="Choisir Dossier", command=self.ChoisireDossier)
        self.load_button.pack(side=tk.LEFT, padx=10)

        self.prev_button = ttk.Button(self.top_frame, text="←", command=self.Prev_image)
        self.prev_button.pack(side=tk.LEFT)

        self.next_button = ttk.Button(self.top_frame, text="→", command=self.Next_image)
        self.next_button.pack(side=tk.LEFT)

        self.canvas = tk.Canvas(self, width=512/2, height=512/2)
        self.canvas.pack()
        
        self.name_var = tk.StringVar()
        self.id_var = tk.StringVar()
        self.fixed_id_var = tk.StringVar()
        self.description_var = tk.StringVar()

        self.entry_frame = ttk.Frame(self)
        self.entry_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(self.entry_frame, text="Nom:").pack(side=tk.LEFT)
        self.name_entry = ttk.Entry(self.entry_frame, textvariable=self.name_var, width=20)
        self.name_entry.pack(side=tk.LEFT)

        ttk.Label(self.entry_frame, text="ID:").pack(side=tk.LEFT)
        self.id_entry = ttk.Entry(self.entry_frame, textvariable=self.id_var, width=5)
        self.id_entry.pack(side=tk.LEFT)

        ttk.Label(self.entry_frame, text="ID Fixe:").pack(side=tk.LEFT)
        self.fixed_id_entry = ttk.Entry(self.entry_frame, textvariable=self.fixed_id_var, width=5)
        self.fixed_id_entry.pack(side=tk.LEFT)

        ttk.Label(self.entry_frame, text="Type 1:").pack(side=tk.LEFT)
        self.type1 = ttk.Combobox(self.entry_frame, values=POKEMON_TYPES, width=10)
        self.type1.pack(side=tk.LEFT)
        
        ttk.Label(self.entry_frame, text="Type 2:").pack(side=tk.LEFT)
        self.type2 = ttk.Combobox(self.entry_frame, values=[""] + POKEMON_TYPES, width=10)
        self.type2.pack(side=tk.LEFT)

        self.desc_entry = ttk.Entry(self, textvariable=self.description_var, width=80)
        self.desc_entry.pack(pady=5)

        self.save_button = ttk.Button(self, text="Sauvegarder", command=self.SaveData)
        self.save_button.pack(pady=10)
    def Prev_image(self):
        self.SaveData()
        self.index = self.index-1
        if self.index<0 :
            self.index = len(self.listeImage)-1
        self.Afficher()
    def Next_image(self):
        self.SaveData()
        self.index=(self.index+1)%len(self.listeImage)
        self.Afficher()
    def Afficher(self):
        chemin_image = self.listeImage[self.index]
        image = Image.open(chemin_image)

        # Redimensionne l'image pour tenir dans le canvas
        image = image.resize((256, 256), Image.Resampling.LANCZOS)
        self.tk_image = ImageTk.PhotoImage(image)

        self.canvas.delete("all")  # Efface l’ancienne image
        self.canvas.create_image(0, 0, anchor="nw", image=self.tk_image)

        # Extraire les données à partir du nom de fichier
        nom_fichier = chemin_image.stem  # sans extension
        extension = chemin_image.suffix
        self.dictionnaire = Renomé(nom_fichier, extension)

        # Remplir les champs avec les données
        self.fixed_id_var.set(self.dictionnaire["iDFixe"])
        self.id_var.set(self.dictionnaire["iDChangable"])
        self.name_var.set(self.dictionnaire["nom"])
        self.type1.set(self.dictionnaire["tipe1"])
        self.type2.set(self.dictionnaire["tipe2"])
        self.description_var.set(self.dictionnaire["description"])
    def SaveData(self,forcer=False, nom="", description="", type1="", type2="", ID=0):
        if forcer == False :
            chemin_image = self.listeImage[self.index]
        else :
            chemin_image = self.listeImage[ID-1]

        dossier = chemin_image.parent
        extension = chemin_image.suffix
        nom_sans_ext = chemin_image.stem

        nouveauNomSansExt = ""
        if forcer == False :
            nouveauNomSansExt = (
                self.id_var.get()
                + "%"
                + self.fixed_id_var.get()
                + "["
                + self.type1.get()
                + ","
                + self.type2.get()
                + "]"
                + self.name_var.get()
                + "!"
            )
        else :
            nouveauNomSansExt = (
                str(ID)
                + "%"
                + str(ID)
                + "["
                + type1
                + ","
                + type2
                + "]"
                + nom
                + "!"
            )
        nouveauNom = nouveauNomSansExt + extension
        nouveau_chemin = chemin_image.with_name(nouveauNom)

        try:
            os.rename(chemin_image, nouveau_chemin)
            self.listeImage[self.index] = nouveau_chemin
        except Exception as e:
            print(f"[ERREUR] Impossible de renommer l'image principale : {e}")
            return

        # 🔄 Recherche d’un fichier PSD associé
        psd_path = dossier / (nom_sans_ext + ".psd")
        if psd_path.exists():
            try:
                nouveau_psd = dossier / (nouveauNomSansExt + ".psd")
                os.rename(psd_path, nouveau_psd)
            except Exception as e:
                print(f"[ERREUR] Impossible de renommer le fichier PSD : {e}")
        else:
            print(f"[INFO] Aucun fichier PSD trouvé pour {nom_sans_ext}")

        if forcer == False :
            EcrireJSON(self.fixed_id_var.get(), self.description_var.get())
        else :
            EcrireJSON(ID, description)
if __name__ == "__main__":
    app = App()
    app.mainloop()

