from flask import Flask, g, render_template, request
from experta import *

app = Flask(__name__)

class psyEngine(KnowledgeEngine):

#Consutructeur
    @DefFacts() 
    def _initial_action(self):
        yield Fact(action="maladie")

#Base des régles
    @Rule(
        Fact(isolement=True),
        Fact(pbConcentration=True),
        Fact(troubleMem=True),
        Fact(perteEnergie=True)
        )
    
    def schizophrenies(self):
        g.decision = "Tu as une sorte de schizophrenie"
        g.conseil  = "La schizophrénie est une maladie du cerveau qui affecte la pensée, les sentiments et les émotions, tout comme les perceptions et les comportements des personnes qui en sont atteintes. Toutes ces fonctions ne sont cependant pas perturbées au même moment et dans la même mesure. De nombreuses personnes souffrant de schizophrénie peuvent avoir un comportement parfaitement normal pendant de longues périodes."
    
    
    @Rule(
        Fact(hyperActif=True),
        Fact(euphorique=True)
        )
    
    def maniaque(self):
        g.decision = " Tu as une sorte de trouble bipolaire - phase maniaque"
        g.conseil  = "Les troubles bipolaires, sont caractérisés par des variations de l'humeur disproportionnées dans leur durée et leur intensité. La gaieté devient euphorie exagérée, la tristesse s'exprime par une dépression profonde. Les troubles du comportement qui accompagnent ces phases désorganisent profondément la vie de la personne touchée et dégradent ses relations familiales et professionnelles. Les troubles bipolaires sont une maladie qui peut être grave et qui nécessite un traitement de longue durée."


    @Rule(
        Fact(tristesse=True),
        Fact(veutMourir=True),
        Fact(perteEnergie=True)
        )
    
    def dépressive(self):
        g.decision = "Tu as une sorte de trouble bipolaire - phase dépressive"
        g.conseil  = "Lorsque la phase dépressive se met en place, le découragement s'installe en quelques jours ou en quelques semaines.D'hyperactive, la personne devient indifférente à tout, abattue. Le suicide est considéré à tort, par le patient, comme le seul moyen de se libérer de sa maladie et de ne plus la faire subir à son entourage."

    @Rule(
        OR(Fact(peurMalAutres=True),
        Fact(peurMaladieGrave=True))
        )
    
    def obsession(self):
        g.decision = "Tu as une sorte d'obsession"
        g.conseil  = "Les obsessions constituent un  trouble mental. Elles se caractérisent par des images intrusives qui surgissent à répétition et qui sont difficiles à chasser de l'esprit. Elles peuvent concerner des thèmes différents comme la saleté, la contamination, le sacrilège, la sexualité ou encore le désordre."

    @Rule(
        Fact(anxiété=True),
        OR(Fact(peurMalAutres=True),
        Fact(peurMaladieGrave=True)))
    
    def toc(self):
        g.decision = "Tu as une sorte de TOC"
        g.conseil  = "Le trouble de la personnalité obsessionnelle compulsive est caractérisé par une préoccupation omniprésente pour l'ordre, le perfectionnisme et le contrôle (sans place pour la flexibilité ou l'efficacité) qui, en fin de compte, interfère avec l'accomplissement d'une tâche."
    

    @Rule(
        Fact(agressif=True),
        Fact(dominant=True),
        Fact(addicté=True)
        )

    def psychopathie(self):
        g.decision = "Tu as une sorte de psychopathie"
        g.conseil  = "La psychopathie est un trouble de la personnalité caractérisé par des désordres émotionnels et des comportements antisociaux. D'un point de vue psychiatrique, ce trouble de la personnalité n'implique pas une forme de criminalité spécifique."
    
    
    @Rule(
        Fact(changeOp=True),
        Fact(menteur=True),
        Fact(plusVisage=True),
        Fact(pbEnfance=True))
    
    def narcissique(self):
        g.decision = "Tu as une sorte de pervers narcissique" 
        g.conseil  ="Un pervers narcissique ou une personne atteinte d'un trouble de la personnalité narcissique est une personne qui a une image dévalorisante d'elle-même et qui se valorise en rabaissant les autres. Cette personne se donne l'apparence d'un être supérieur aux autres et ressent un besoin exacerbé de se faire admirer. Elle manipule les proches de son entourage et ne ressent aucune culpabilité lorsqu'elle blesse les autres."
    
    @Rule(
        Fact(tristesse=True),
        Fact(sentimentVide=True)
        )
    
    def humeurMorose(self):
        g.decision = "Tu as un humeur morose" 
        g.conseil  = "Une personne atteinte d'un trouble de l'humeur ressent les émotions négatives plus intensément et pendant plus longtemps que la plupart des gens. Elle peut sentir qu'elle a plus de mal à maîtriser ses émotions, ce qui nuit à sa santé mentale et à sa santé physique, en plus d'influencer ses comportements"
    
    @Rule(
        Fact(dominant=True),
        Fact(isolement=True),
        Fact(agressif=True)
        )
    
    def paranoia(self):
        g.decision = "Tu as une sorte de paranoïa" 
        g.conseil  = "La paranoïa est un trouble mental caractérisé par une méfiance et une suspicion excessive à l'égard d'autrui, même lorsqu'il n'y a aucune raison de se méfier. Le comportement de la personne paranoïaque peut sembler étrange ou inhabituel aux yeux des autres. "
    
    
    @Rule(
        Fact(tristesse=True),
        Fact(sentimentVide=True),
        Fact(sommeil=True),
        Fact(perteEnergie=True)
        )
    
    def depression(self):
        g.decision = "Tu as une sorte de dépression"
        g.conseil  = "La dépression est une maladie mentale qui affecte l'humeur d'une personne, la façon dont elle se sent. L'humeur influence la perception que les personnes ont d'elles-mêmes, leurs relations avec les autres et leur interaction avec le monde environnant. C'est bien plus qu'une « mauvaise journée » ou « broyer du noir ». Sans aide, par exemple un traitement, la dépression peut durer longtemps."
    

@app.route('/')

#Les questions existants
def index():
    questions = {
        1: "Avez-vous un probléme de concentration ?",
        2: "Avez-vous des troubles de mémoire ?",
        3: "Restez-vous seul la plupart du temps?",
        4: "Etes vous hyperactif ?",
        5: "Etes-vous euphorique ?",
        6: "Avez-vous envie de mourir?",
        7: "Êtes-vous anxieux excessif ?",
        8: "Avez vous vecu une profonde tristesse ?",
        9: "Avez-vous peur de faire du mal aux autres ?",
        10: "Avez-vous peur d'attraper une maladie grave ?",
        11: "Êtes-vous dominant(e)?",
        12: "Êtes-vous agressif(ve)?",
        13: "Êtes-vous un consommateur d'alcool, de drogue ou de médicaments ?",
        14: "Étiez-vous un enfant négligé ou abusé ou surprotegé ?",
        15: "Pensez-vous que vous avez plusieurs visages ?",
        16: "Êtes-vous une personne qui change fréquemment d'opinion ?",
        17: "Avez vous déja menti ?",
        18: "Avez vous des troubles du sommeil ?",
        19: "Vous sentez-vous vide ?",
        20: "Avez-vous l'impression d'avoir perdu l'énergie ?"
    }
    return render_template('index.html', questions=questions)

@app.route('/report', methods=['POST', "GET"])

#Les réponses aux questions
def report():
    questions_answers = {}
    for i in range(1,21):
        questions_answers[i] = bool(int(request.form['q'+str(i)]))
    
#Le moteur d'inférance
    engine = psyEngine()
    engine.reset()

    engine.declare(Fact(
        pbConcentration     = questions_answers[1],
        troubleMem          = questions_answers[2],
        isolement           = questions_answers[3],
        hyperActif          = questions_answers[4],
        euphorique          = questions_answers[5],
        veutMourir          = questions_answers[6],
        anxiété             = questions_answers[7],
        tristesse           = questions_answers[8],
        peurMalAutres       = questions_answers[9],
        peurMaladieGrave    = questions_answers[10],
        dominant            = questions_answers[11],
        agressif            = questions_answers[12],
        addicté             = questions_answers[13],
        pbEnfance           = questions_answers[14],
        plusVisage          = questions_answers[15],
        changeOp            = questions_answers[16],
        menteur             = questions_answers[17],
        sommeil             = questions_answers[18],
        sentimentVide       = questions_answers[19],
        perteEnergie       = questions_answers[20],
    ))

#Runnig du moteur d'inférance
    engine.run()

#L'envoi des parametres(decision et conseil) à l'interface pour les afficher
    decision =  g.decision if hasattr(g, 'decision') else "Tu a un comportement sain" # si on n'a pas de decision
    conseil  =  g.conseil if hasattr(g, 'conseil') else "" # si on n'a pas de conseil
    list_param =[decision, conseil]
    return render_template('report.html', list_param=list_param)
