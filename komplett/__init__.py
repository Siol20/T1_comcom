import random
import csv
from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'komplett'
    players_per_group = None
    TASKS = ['hex', 'rec', 'sm', 'svo']
    num_rounds = len(TASKS)
    endowment = cu(400)
    multiplier = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    h1 = models.IntegerField(
        label="Wenn ich wüsste, dass ich niemals erwischt werde, wäre ich bereit, eine Million zu stehlen.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h2 = models.IntegerField(
        label="Ich mache mir viel weniger Sorgen als die meisten Leute.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h3 = models.IntegerField(
        label="Ich habe selten, wenn überhaupt, Schlafprobleme durch Stress oder Angst.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h4 = models.IntegerField(
        label="Ich bin fast immer voller Energie.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h5 = models.IntegerField(
        label="Ich versuche, Notleidende großzügig zu unterstützen.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h6 = models.IntegerField(
        label="Andere machen oft mit mir zusammen Witze über die Unordentlichkeit meines Zimmers oder Schreibtisches.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h7 = models.IntegerField(
        label="Die meisten Leute sind aufgedrehter und dynamischer als ich es im Allgemeinen bin.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h8 = models.IntegerField(
        label="Andere sagen mir manchmal, dass ich zu kritisch gegenüber anderen bin.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h9 = models.IntegerField(
        label="Ich mache viele Fehler, weil ich nicht nachdenke, bevor ich handele.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h10 = models.IntegerField(
        label="Das erste, was ich an einem neuen Ort tue, ist, Freundschaften zu schließen.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h11 = models.IntegerField(
        label="Ich ziehe Berufe, in denen man sich aktiv mit anderen Menschen auseinandersetzt, solchen vor, in "
              "denen man alleine arbeitet.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h12 = models.IntegerField(
        label="Andere sagen mir oft, dass ich versuchen sollte, etwas fröhlicher zu sein.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h13 = models.IntegerField(
        label="Ich will, dass alle wissen, dass ich eine wichtige angesehene Person bin.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h14 = models.IntegerField(
        label="Ich wäre von einem Buch über die Geschichte der Wissenschaft und Technik sehr gelangweilt.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h15 = models.IntegerField(
        label="Es fällt mir schwer, jemandem vollkommen zu vergeben, der mir etwas Gemeines angetan hat.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h16 = models.IntegerField(
        label="Ich kann manchmal nichts dagegen machen, dass ich mir über kleine Dinge Sorgen mache.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h17 = models.IntegerField(
        label="Ich würde nicht vortäuschen, jemanden zu mögen, nur um diese Person dazu zu bringen, "
              "mir Gefälligkeiten zu erweisen.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h18 = models.IntegerField(
        label="Ich würde niemals Bestechungsgeld annehmen, auch wenn es sehr viel wäre.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h19 = models.IntegerField(
        label="Ich finde es langweilig, über Philosophie zu diskutieren.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h20 = models.IntegerField(
        label="Ich lasse nicht zu, dass meine Impulse mein Verhalten dominieren.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h21 = models.IntegerField(
        label="Es fällt mir schwer, mit anderen einen Kompromiss einzugehen, wenn ich überzeugt bin, "
              "dass ich Recht habe.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h22 = models.IntegerField(
        label="Andere nennen mich oft einen Perfektionisten.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h23 = models.IntegerField(
        label="Ich vermeide es, mit anderen Leuten Small Talk zu halten.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h24 = models.IntegerField(
        label="Wenn ich von einer Person, die ich nicht mag, etwas will, verhalte ich mich dieser Person gegenüber "
              "sehr nett, um es zu bekommen.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h25 = models.IntegerField(
        label="Ich ziehe es vor, das zu tun, was mir gerade in den Sinn kommt, anstatt an einem Plan festzuhalten.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h26 = models.IntegerField(
        label="Die meisten Leute werden schneller ärgerlich als ich.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h27 = models.IntegerField(
        label="Ich akzeptiere im Allgemeinen die Schwächen anderer, ohne mich darüber zu beschweren.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h28 = models.IntegerField(
        label="Ich würde in Versuchung geraten, Diebesgut zu kaufen, wenn ich knapp bei Kasse wäre.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h29 = models.IntegerField(
        label="Ich plane im Voraus und organisiere, damit in letzter Minute kein Zeitdruck aufkommt.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h30 = models.IntegerField(
        label="Mir gefällt der Gedanke, dass nur die Starken überleben sollten.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h31 = models.IntegerField(
        label="Ich versuche immer, fehlerfrei zu arbeiten, auch wenn es Zeit kostet.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h32 = models.IntegerField(
        label="Ich fühle starke Emotionen, wenn jemand, der mir nahe steht, für eine längere Zeit weggeht.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h33 = models.IntegerField(
        label="Man hat mir schon oft gesagt, dass ich eine gute Vorstellungskraft habe.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h34 = models.IntegerField(
        label="Ich bin daran interessiert, etwas über die Geschichte und Politik anderer Länder zu lernen.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h35 = models.IntegerField(
        label="Ich bin gewöhnlich ziemlich flexibel in meinen Ansichten, wenn andere Leute mir nicht zustimmen.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h36 = models.IntegerField(
        label="Ich fühle mich nicht ganz behaglich, wenn ich vor einer Gruppe von Leuten spreche.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h37 = models.IntegerField(
        label="Ich diskutiere selten meine Probleme mit anderen Leuten.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h38 = models.IntegerField(
        label="Ich halte mich selber für eine etwas exzentrische Person.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h39 = models.IntegerField(
        label="Ich bin eine ganz normale Person, die nicht besser ist als andere.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h40 = models.IntegerField(
        label="Wenn ich die Gelegenheit dazu hätte, würde ich gerne ein Konzert mit klassischer Musik besuchen.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h41 = models.IntegerField(
        label="Es würde mich nicht stören, jemandem zu schaden, den ich nicht mag.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h42 = models.IntegerField(
        label="Im Allgemeinen bin ich mit mir ziemlich zufrieden.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h43 = models.IntegerField(
        label="Ich denke, dass es Zeitverschwendung ist, radikalen Ideen Aufmerksamkeit zu schenken.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h44 = models.IntegerField(
        label="Ich habe Mitgefühl mit Menschen, die weniger Glück haben als ich.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h45 = models.IntegerField(
        label="Manchmal mag ich es, einfach nur dem Wind zuzusehen, wie er durch die Bäume bläst.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h46 = models.IntegerField(
        label="In sozialen Situationen bin ich gewöhnlich der, der den ersten Schritt macht.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h47 = models.IntegerField(
        label="Wenn ich an irgendetwas arbeite, beachte ich kleine Details nicht allzu sehr.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h48 = models.IntegerField(
        label="Ich habe selten Wut im Bauch, nicht mal gegen Leute, die mich sehr ungerecht behandelt haben.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h49 = models.IntegerField(
        label="Wenn mir andere sagen, dass ich falsch liege, ist meine erste Reaktion, mit ihnen zu streiten.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h50 = models.IntegerField(
        label="Wenn jemand, den ich gut kenne, unglücklich ist, kann ich den Schmerz dieser Person fast selber spüren.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h51 = models.IntegerField(
        label="Ich versuche, die Gefühle anderer zu respektieren.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h52 = models.IntegerField(
        label="Wenn ich arbeite, habe ich manchmal Schwierigkeiten, weil ich unorganisiert bin.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h53 = models.IntegerField(
        label="Andere halten mich für jähzornig.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h54 = models.IntegerField(
        label="Ich würde in die Versuchung geraten, Falschgeld zu benutzen, wenn ich sicher sein könnte, "
              "damit durchzukommen.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h55 = models.IntegerField(
        label="Ich würde gerne dabei gesehen werden, wie ich in einem sehr teuren Auto herumfahre.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h56 = models.IntegerField(
        label="Ich putze mein Büro oder zuhause ziemlich oft.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h57 = models.IntegerField(
        label="Wenn ich wegen einer schmerzvollen Erfahrung leide, brauche ich jemanden, der mich tröstet.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h58 = models.IntegerField(
        label="Ich will nicht, dass andere Leute mich behandeln, als ob ich ihnen überlegen sei.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h59 = models.IntegerField(
        label="Bei Gruppentreffen sage ich nur selten meine Meinung.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h60 = models.IntegerField(
        label="Ich glaube, dass die meisten Menschen einige Aspekte meines Charakters mögen.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h61 = models.IntegerField(
        label="Der Besuch einer Kunstausstellung würde mich ziemlich langweilen.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h62 = models.IntegerField(
        label="Es stört mich nicht, Arbeiten zu erledigen, die gefährlich sind.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h63 = models.IntegerField(
        label="Ich wünsche mir einen Beruf, der Routine verlangt, anstatt einen, der Kreativität fordert.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h64 = models.IntegerField(
        label="Ich würde keine Schmeicheleien benutzen, um eine Gehaltserhöhung zu bekommen oder befördert zu "
              "werden, auch wenn ich wüsste, dass es erfolgreich wäre.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h65 = models.IntegerField(
        label="Man hält mich für einen hartherzigen Menschen.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h66 = models.IntegerField(
        label="Ich werde selten wütend, selbst wenn andere mich ziemlich schlecht behandeln.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h67 = models.IntegerField(
        label=" Ich könnte weinen, wenn ich andere Personen sehe, die weinen.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h68 = models.IntegerField(
        label="Ich würde es genießen, ein Kunstwerk zu schaffen, etwa einen Roman, ein Lied oder ein Gemälde.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h69 = models.IntegerField(
        label="Wenn ich arbeite, setze ich mir oft ehrgeizige Ziele.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h70 = models.IntegerField(
        label="Wenn ich von jemandem etwas will, lache ich auch noch über dessen schlechteste Witze.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h71 = models.IntegerField(
        label="Wenn ich mir um irgendetwas Sorgen mache, will ich meine Sorgen mit einer anderen Person teilen.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h72 = models.IntegerField(
        label="Ich kann mit schwierigen Situationen umgehen, ohne dass ich emotionale Unterstützung von "
              "irgendjemandem brauche.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h73 = models.IntegerField(
        label="Ich bin der Meinung, dass ich nicht beliebt bin.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h74 = models.IntegerField(
        label="Wenn ich mir ein Ziel setze, gebe ich oft auf, bevor ich es erreicht habe.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h75 = models.IntegerField(
        label="Ich bin ein weichherziger Mensch.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h76 = models.IntegerField(
        label="Ich mag es, Landkarten von anderen Orten zu betrachten.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h77 = models.IntegerField(
        label="An den meisten Tagen bin ich fröhlich und optimistisch.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h78 = models.IntegerField(
        label="Ich habe es noch nie wirklich gemocht, eine Enzyklopädie durchzublättern.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h79 = models.IntegerField(
        label="Es fällt mir schwer, mich zu beherrschen, wenn Leute mich beleidigen.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h80 = models.IntegerField(
        label="Andere sagen mir manchmal, dass ich zu dickköpfig bin.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h81 = models.IntegerField(
        label="Ich denke, dass ich mehr Respekt verdiene als ein durchschnittlicher Mensch.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h82 = models.IntegerField(
        label="Ich halte mich nicht für einen künstlerischen oder kreativen Menschen.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h83 = models.IntegerField(
        label="Selbst in einem Notfall würde ich nicht in Panik geraten.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h84 = models.IntegerField(
        label="Oft kontrolliere ich meine Arbeit mehrfach, um alle Fehler zu finden.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h85 = models.IntegerField(
        label="Ich hätte Angst, wenn ich bei schlechten Wetterbedingungen verreisen müsste.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h86 = models.IntegerField(
        label="Manchmal habe ich den Eindruck, dass ich wertlos bin.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h87 = models.IntegerField(
        label="Wenn es um körperliche Gefahren geht, bin ich sehr ängstlich.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h88 = models.IntegerField(
        label="Ich arbeite nur so viel wie nötig, um gerade so durchzukommen.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h89 = models.IntegerField(
        label="Ich treffe Entscheidungen eher aus dem Bauch heraus als durch sorgfältiges Nachdenken.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h90 = models.IntegerField(
        label="Meine Einstellung gegenüber Personen, die mich schlecht behandelt haben, ist „vergeben und vergessen“.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h91 = models.IntegerField(
        label="Ich neige dazu, nachsichtig zu sein, wenn ich andere beurteile.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h92 = models.IntegerField(
        label="Ich würde gerne in einer sehr teuren, angesehenen Nachbarschaft wohnen.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h93 = models.IntegerField(
        label="Es würde mir viel Freude bereiten, teure Luxusgüter zu besitzen.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h94 = models.IntegerField(
        label="Ich werde sehr unruhig, wenn ich auf eine wichtige Entscheidung warte.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h95 = models.IntegerField(
        label="Ich würde meine Zeit nicht damit verbringen, einen Gedichtband zu lesen.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h96 = models.IntegerField(
        label="Wenn mich jemand einmal betrogen hat, werde ich dieser Person gegenüber immer misstrauisch bleiben.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h97 = models.IntegerField(
        label="Ich würde mich schrecklich fühlen, wenn ich jemanden verletzen müsste.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h98 = models.IntegerField(
        label="Ich bleibe emotionslos, selbst in Situationen, in denen die meisten Leute sehr sentimental werden.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h99 = models.IntegerField(
        label="Wenn ich in einer Gruppe von Leuten bin, bin ich oft derjenige, der im Namen der Gruppe spricht.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h100 = models.IntegerField(
        label="Ich mag Leute, die unkonventionelle Ideen haben.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h101 = models.IntegerField(
        label="Ich treibe mich oft selbst sehr stark an, wenn ich versuche, ein Ziel zu erreichen.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h102 = models.IntegerField(
        label="Selbst wenn Leute viele Fehler machen, sage ich nur selten etwas Negatives.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h103 = models.IntegerField(
        label="Ich genieße es, viele Leute um mich herum zu haben, mit denen ich reden kann.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h104 = models.IntegerField(
        label="Viel Geld zu haben ist nicht besonders wichtig für mich.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    hexaco_check_pass = models.BooleanField(
        initial=False
    )
    PosRec_1 = models.IntegerField(label="Ich bin bereit, persönliche Kosten in Kauf zu nehmen, "
                                         "um jemandem zu helfen, der mir zuvor auch schon einmal geholfen hat. ",
                                   widget=widgets.RadioSelect, choices=[[1, 'stimme überhaupt nicht zu'], [2, ''],
                                                                        [3, ''], [4, 'stimme weder zu noch nicht zu'],
                                                                        [5, ''], [6, ''], [7, 'stimme stark zu']])
    PosRec_2 = models.IntegerField(label="Wenn mir jemand einen Gefallen tut, bin ich bereit, der Person ebenfalls "
                                         "einen Gefallen zu tun. ", widget=widgets.RadioSelect,
                                   choices=[1, 2, 3, 4, 5, 6, 7])
    PosRec_3 = models.IntegerField(label="Wenn mir jemand bei der Arbeit/im Studium bei etwas hilft, ist es mir eine "
                                         "Freude, der betreffenden Person bei Gelegenheit ebenfalls zu helfen. ",
                                   widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5, 6, 7])
    PosRec_4 = models.IntegerField(label="Ich bin bereit, eine langweilige Arbeit zu erledigen, um mich bei jemandem "
                                         "zu revanchieren, der mir zuvor auch schon einmal geholfen hat. ",
                                   widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5, 6, 7])
    PosRec_5 = models.IntegerField(label="Wenn mir jemand einen Gefallen tut, fühle ich mich verpflichtet, den "
                                         "Gefallen zu erwidern. ", widget=widgets.RadioSelect,
                                   choices=[1, 2, 3, 4, 5, 6, 7])
    PosRec_6 = models.IntegerField(label="Wenn mich jemand höflich um eine Information bittet, bin ich gerne bereit, "
                                         "zu helfen. ", widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5, 6, 7])
    PosRec_7 = models.IntegerField(label="Wenn mir jemand Geld geliehen hat, habe ich das Gefühl, dass ich der Person "
                                         "etwas mehr Geld zurückgeben sollte, als sie mir ursprünglich ausgeliehen "
                                         "hatte.", widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5, 6, 7])
    PosRec_8 = models.IntegerField(label="Wenn mir jemand die Gewinnzahl in einer Lotterie richtig vorhersagen "
                                         "würde, dann würde ich der Person sicherlich einen Teil des Gewinns "
                                         "abgeben. ", widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5, 6, 7])
    PosRec_9 = models.IntegerField(label="Ich bin bereit, besondere Anstrengungen zu unternehmen, um einer Person zu "
                                         "helfen, die mir zuvor auch schon einmal geholfen hat. ",
                                   widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5, 6, 7])
    NegRec_1 = models.IntegerField(label="Wenn mir ein ernsthafter Schaden zugefügt wird, werde ich mich dafür "
                                         "baldmöglichst rächen, egal welche Kosten ich dafür in Kauf nehmen muss. ",
                                   widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5, 6, 7])
    NegRec_2 = models.IntegerField(label="Ich bin bereit, Zeit und Mühe aufzubringen, um mich für eine unfaire "
                                         "Behandlung zu revanchieren. ", widget=widgets.RadioSelect,
                                   choices=[1, 2, 3, 4, 5, 6, 7])
    NegRec_3 = models.IntegerField(label="Ich bin nett und freundlich, wenn andere sich mir gegenüber gut verhalten, "
                                         "andernfalls halte ich mich an die Regel „wie du mir - so ich dir“. ",
                                   widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5, 6, 7])
    NegRec_4 = models.IntegerField(label="Wenn mich jemand in eine schwierige Lage bringt, werde ich ihm/ihr bei "
                                         "Gelegenheit dasselbe antun. ", widget=widgets.RadioSelect,
                                   choices=[1, 2, 3, 4, 5, 6, 7])
    NegRec_5 = models.IntegerField(label="Wenn mich jemand beleidigt, erwidere ich die Beleidigung. ",
                                   widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5, 6, 7])
    NegRec_6 = models.IntegerField(label="Wenn sich jemand mir gegenüber unfair verhält, ziehe ich es vor, es der "
                                         "Person zurückzuzahlen, anstatt eine Entschuldigung von der Person zu "
                                         "akzeptieren.", widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5, 6, 7])
    NegRec_7 = models.IntegerField(label="Ich würde einer Person, die sich mir gegenüber zuvor schlecht verhalten "
                                         "hat, keinen Gefallen tun, selbst dann nicht, wenn ich dadurch einen "
                                         "persönlichen Gewinn verpassen würde. ", widget=widgets.RadioSelect,
                                   choices=[1, 2, 3, 4, 5, 6, 7])
    NegRec_8 = models.IntegerField(label="Wenn mir gegenüber jemand unhöflich ist, werde ich auch unhöflich. ",
                                   widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5, 6, 7])
    NegRec_9 = models.IntegerField(label="Wie ich andere Personen behandle, hängt stark davon ab, wie die "
                                         "betreffenden Personen mich behandeln. ", widget=widgets.RadioSelect,
                                   choices=[1, 2, 3, 4, 5, 6, 7])
    BelRec_1 = models.IntegerField(label="Jemandem zu helfen ist die beste Maßnahme, um sicher sein zu können, dass "
                                         "die betreffende Person einem selbst in der Zukunft auch einmal Hilfe "
                                         "leisten wird. ", widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5, 6, 7])
    BelRec_2 = models.IntegerField(label="Ich verhalte mich anderen gegenüber nicht schlecht, um zu vermeiden, dass "
                                         "sie sich mir gegenüber einmal schlecht verhalten werden. ",
                                   widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5, 6, 7])
    BelRec_3 = models.IntegerField(label="Ich fürchte mich vor den Reaktionen von einer Person, die ich zuvor "
                                         "schlecht behandelt habe. ", widget=widgets.RadioSelect,
                                   choices=[1, 2, 3, 4, 5, 6, 7])
    BelRec_4 = models.IntegerField(label="Wenn ich hart arbeite, erwarte ich, dass ich dafür etwas zurückbekomme. ",
                                   widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5, 6, 7])
    BelRec_5 = models.IntegerField(label="Wenn ich jemandem Komplimente mache, erwarte ich, dass die Person das "
                                         "gleiche tut. ", widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5, 6, 7])
    BelRec_6 = models.IntegerField(label="Ich vermeide es, unhöflich zu sein, weil ich nicht möchte, dass andere mir "
                                         "gegenüber unhöflich sind. ", widget=widgets.RadioSelect,
                                   choices=[1, 2, 3, 4, 5, 6, 7])
    BelRec_7 = models.IntegerField(label="Wenn ich Touristen helfe, erwarte ich, dass sie sich bei mir freundlich "
                                         "dafür bedanken. ", widget=widgets.RadioSelect,
                                   choices=[1, 2, 3, 4, 5, 6, 7])
    BelRec_8 = models.IntegerField(label="Wenn es offensichtlich ist, dass ich jemanden schlecht behandle, wird die "
                                         "betreffende Person danach auf Rache aus sein. ",
                                   widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5, 6, 7])
    BelRec_9 = models.IntegerField(label="Wenn ich in einem Restaurant kein gutes Trinkgeld gebe, gehe ich davon "
                                         "aus, dass ich dort in der Zukunft keinen guten Service erwarten kann. ",
                                   widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5, 6, 7])
    rec_check_pass = models.BooleanField(
        initial=False
    )
    time_end = models.StringField()
    costs = models.CurrencyField(
        initial=0
    )
    compr_check_pass = models.BooleanField(
        initial=False
    )
    compr_check_1st_1 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        blank=True
    )
    compr_check_1st_2 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        blank=True
    )
    compr_check_2nd_1 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        blank=True
    )
    compr_check_2nd_2 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        blank=True
    )
    compr_check_3rd_1 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        blank=True
    )
    compr_check_3rd_2 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        blank=True
    )
    contribution = models.CurrencyField(
        min=0,
        max=Constants.endowment
    )
    cond_coop_0 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label='0 Cent'
    )
    cond_coop_20 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label='20 Cent'
    )
    cond_coop_40 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label='40 Cent'
    )
    cond_coop_60 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label='60 Cent'
    )
    cond_coop_80 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label='80 Cent'
    )
    cond_coop_100 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label='100 Cent'
    )
    cond_coop_120 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label='120 Cent'
    )
    cond_coop_140 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label='140 Cent'
    )
    cond_coop_160 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label='160 Cent'
    )
    cond_coop_180 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label='180 Cent'
    )
    cond_coop_200 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label='200 Cent'
    )
    cond_coop_220 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label='220 Cent'
    )
    cond_coop_240 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label='240 Cent'
    )
    cond_coop_260 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label='260 Cent'
    )
    cond_coop_280 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label='280 Cent'
    )
    cond_coop_300 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label='300 Cent'
    )
    cond_coop_320 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label='320 Cent'
    )
    cond_coop_340 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label='340 Cent'
    )
    cond_coop_360 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label='360 Cent'
    )
    cond_coop_380 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label='380 Cent'
    )
    cond_coop_400 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label='400 Cent'
    )
    sm_check_pass = models.BooleanField(
        initial=False
    )
    svo_choice_1 = models.IntegerField(blank=True)
    svo_choice_2 = models.IntegerField(blank=True)
    svo_choice_3 = models.IntegerField(blank=True)
    svo_choice_4 = models.IntegerField(blank=True)
    svo_choice_5 = models.IntegerField(blank=True)
    svo_choice_6 = models.IntegerField(blank=True)
    svo_choice_7 = models.IntegerField(blank=True)
    svo_choice_8 = models.IntegerField(blank=True)
    svo_choice_9 = models.IntegerField(blank=True)
    svo_choice_10 = models.IntegerField(blank=True)
    svo_choice_11 = models.IntegerField(blank=True)
    svo_choice_12 = models.IntegerField(blank=True)
    svo_choice_13 = models.IntegerField(blank=True)
    svo_choice_14 = models.IntegerField(blank=True)
    svo_choice_15 = models.IntegerField(blank=True)
    svo_tot_ego = models.IntegerField()
    svo_tot_alter = models.IntegerField()
    svo_mean_ego = models.FloatField()
    svo_mean_alter = models.FloatField()
    svo_ratio = models.FloatField()
    svo_angle = models.FloatField()
    svo_check_pass = models.BooleanField(
        initial=False
    )


# FUNCTIONS
def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        for p in subsession.get_players():
            round_numbers = list(range(1, Constants.num_rounds + 1))
            random.shuffle(round_numbers)
            task_rounds = dict(zip(Constants.TASKS, round_numbers))
            # print('player', p.id_in_subsession)
            # print('task_rounds is', task_rounds)
            p.participant.task_rounds = task_rounds

# ADMINPAGE
def vars_for_admin_report(subsession):
    with open('LabIds/CountParticipation.txt', 'r') as file:
        count_participants_condition = int(file.read())

    return dict(
        count_participants_condition = count_participants_condition
    )


# PAGES
class Hexaco_Einleitung (Page):
    def before_next_page(player, timeout_happened):
        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['hex']

    def vars_for_template(player: Player):
        rec_check = False
        for p in player.in_all_rounds():
            if p.rec_check_pass:
                rec_check = True
        return dict(
            rec_check = rec_check
        )


class Hexaco(Page):
    form_model = 'player'
    random_hexaco_items = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9', 'h10', 'h11', 'h12', 'h13', 'h14',
                           'h15', 'h16', 'h17', 'h18', 'h19', 'h20', 'h21', 'h22', 'h23', 'h24', 'h25', 'h26',
                           'h27', 'h28', 'h29', 'h30', 'h31', 'h32', 'h33', 'h34', 'h35', 'h36', 'h37', 'h38',
                           'h39', 'h40', 'h41', 'h42', 'h43', 'h44', 'h45', 'h46', 'h47', 'h48', 'h49', 'h50',
                           'h51', 'h52', 'h53', 'h54', 'h55', 'h56', 'h57', 'h58', 'h59', 'h60', 'h61', 'h62',
                           'h63', 'h64', 'h65', 'h66', 'h67', 'h68', 'h69', 'h70', 'h71', 'h72', 'h73', 'h74',
                           'h75', 'h76', 'h77', 'h78', 'h79', 'h80', 'h81', 'h82', 'h83', 'h84', 'h85', 'h86',
                           'h87', 'h88', 'h89', 'h90', 'h91', 'h92', 'h93', 'h94', 'h95', 'h96', 'h97', 'h98',
                           'h99', 'h100']
    import random
    random.shuffle(random_hexaco_items)
    form_fields = random_hexaco_items

    def before_next_page(player, timeout_happened):
        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        player.hexaco_check_pass = True

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['hex']

class Rec_Einleitung(Page):
    def before_next_page(player, timeout_happened):
        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['rec']

    def vars_for_template(player: Player):
        hexaco_check = False
        for p in player.in_all_rounds():
            if p.hexaco_check_pass:
                hexaco_check = True
        return dict(
            hexaco_check = hexaco_check
        )

class Reciprocityscale(Page):
    form_model = 'player'
    random_reciprocity_scales = ['PosRec_1', 'PosRec_2', 'PosRec_3', 'PosRec_4', 'PosRec_5', 'PosRec_6', 'PosRec_7', 'PosRec_8',
                   'PosRec_9', 'NegRec_1', 'NegRec_2', 'NegRec_3', 'NegRec_4', 'NegRec_5', 'NegRec_6', 'NegRec_7',
                   'NegRec_8', 'NegRec_9', 'BelRec_1', 'BelRec_2', 'BelRec_3', 'BelRec_4', 'BelRec_5', 'BelRec_6',
                   'BelRec_7', 'BelRec_8', 'BelRec_9']
    import random
    random.shuffle(random_reciprocity_scales)
    form_fields = random_reciprocity_scales

    def before_next_page(player, timeout_happened):
        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        player.rec_check_pass = True


    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['rec']

class SM_Einleitung(Page):
    def before_next_page(player, timeout_happened):
        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['sm']

    def vars_for_template(player: Player):
        svo_check = False
        for p in player.in_all_rounds():
            if p.svo_check_pass:
                svo_check = True
        return dict(
            svo_check = svo_check
        )

class Instructions(Page):
    def before_next_page(player, timeout_happened):
        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['sm']

class Szenario1(Page):
    def before_next_page(player, timeout_happened):
        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['sm']

class Szenario2(Page):
    def before_next_page(player, timeout_happened):
        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['sm']

class Szenario3(Page):
    def before_next_page(player, timeout_happened):
        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['sm']

class ComprehensionCheck(Page):
    form_model = 'player'
    form_fields = ['compr_check_1st_1','compr_check_1st_2']

    def error_message(player, values):
        if values['compr_check_1st_1'] is None or values["compr_check_1st_2"] is None:
            return 'Bitte füllen Sie alle Felder aus.'

    def before_next_page(player, timeout_happened):
        if player.compr_check_1st_1 == 400 and player.compr_check_1st_2 == 0:
            player.compr_check_pass = True
        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['sm']

class ComprehensionCheck2(Page):
    form_model = 'player'
    form_fields = ['compr_check_2nd_1','compr_check_2nd_2']

    def is_displayed(player: Player):
        participant = player.participant
        return (player.compr_check_pass != True and player.round_number == participant.task_rounds['sm'])

    def error_message(player, values):
        if (values['compr_check_2nd_1'] is None and player.compr_check_1st_1 != 400) or (values["compr_check_2nd_2"] is None and player.compr_check_1st_2 != 0):
            return 'Bitte füllen Sie alle Felder aus.'

    def before_next_page(player, timeout_happened):
        if (player.compr_check_1st_1 == 400 or player.compr_check_2nd_1 == 400) and (player.compr_check_1st_2 == 0 or player.compr_check_2nd_2 == 0):
            player.compr_check_pass = True
        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

class ComprehensionCheck3(Page):
    form_model = 'player'
    form_fields = ['compr_check_3rd_1','compr_check_3rd_2']

    def is_displayed(player: Player):
        participant = player.participant
        return (player.compr_check_pass != True and player.round_number == participant.task_rounds['sm'])

    def error_message(player, values):
        if (values['compr_check_3rd_1'] is None and player.compr_check_1st_1 != 400 and player.compr_check_2nd_1 != 400) or (values["compr_check_3rd_2"] is None and player.compr_check_1st_2 != 0 and player.compr_check_2nd_2 != 0):
            return 'Bitte füllen Sie alle Felder aus.'

    def before_next_page(player, timeout_happened):
        if (player.compr_check_1st_1 == 400 or player.compr_check_2nd_1 == 400 or player.compr_check_3rd_1 == 400) and (player.compr_check_1st_2 == 0 or player.compr_check_2nd_2 == 0 or player.compr_check_3rd_2 == 0):
            player.compr_check_pass = True
        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

class PartA(Page):
    form_model = 'player'
    form_fields = ['contribution']

    def error_message(player, values):
        if values['contribution'] % 10 != 0:
            return 'Bitte geben Sie einen durch 10 teilbaren Betrag ein.'

    def before_next_page(player, timeout_happened):
        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['sm']

class PartB(Page):
    form_model = 'player'
    form_fields = ['cond_coop_0','cond_coop_20','cond_coop_40','cond_coop_60','cond_coop_80','cond_coop_100','cond_coop_120','cond_coop_140','cond_coop_160','cond_coop_180','cond_coop_200','cond_coop_220','cond_coop_240','cond_coop_260','cond_coop_280','cond_coop_300','cond_coop_320','cond_coop_340','cond_coop_360','cond_coop_380','cond_coop_400']

    def error_message(player, values):
        for i in values:
            if values[i] % 10 != 0:
                return 'Bitte geben Sie nur durch 10 teilbare Beträge ein.'

    def before_next_page(player, timeout_happened):
        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        player.sm_check_pass = True

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['sm']


class SVO_Einleitung (Page):
    def before_next_page(player, timeout_happened):
        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['svo']

    def vars_for_template(player: Player):
        sm_check = False
        for p in player.in_all_rounds():
            if p.sm_check_pass:
                sm_check = True
        return dict(
            sm_check = sm_check
        )


class SVOExample(Page):

    def before_next_page(player, timeout_happened):
        with open(player.session.config['svo_file']) as f:
            r = csv.reader(f, delimiter=";")
            c = [line for line in r]
            h = c[0]
            d = [dict(zip(h, l)) for l in c[1:]]
            player.session.vars["SVO_Fullx3"] = [
                [[r, l["A" + str(i + 1)], l["B" + str(i + 1)]] for i in range(int(l["N"]))]
                for r, l in enumerate(d)]
        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['svo']

class SVOTask(Page):
    form_model = 'player'
    form_fields = ["svo_choice_1", "svo_choice_2", "svo_choice_3", "svo_choice_4", "svo_choice_5", "svo_choice_6", "svo_choice_7", "svo_choice_8", "svo_choice_9", "svo_choice_10", "svo_choice_11", "svo_choice_12", "svo_choice_13", "svo_choice_14", "svo_choice_15", "svo_tot_ego", "svo_tot_alter", "svo_mean_ego", "svo_mean_alter", "svo_ratio", "svo_angle"]

    @staticmethod
    def vars_for_template(player):
        SVO = player.session.vars["SVO_Fullx3"]
        return dict(
            SVO = SVO
        )

    def before_next_page(player, timeout_happened):
        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        player.svo_check_pass = True

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['svo']


page_sequence = [
    Hexaco_Einleitung,
    Hexaco,
    Rec_Einleitung,
    Reciprocityscale,
    SM_Einleitung,
    Instructions,
    Szenario1,
    Szenario2,
    Szenario3,
    ComprehensionCheck,
    ComprehensionCheck2,
    ComprehensionCheck3,
    PartA,
    PartB,
    SVO_Einleitung,
    SVOExample,
    SVOTask,
]
