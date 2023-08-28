import re

all_user_entries = [["I", "I", "I", "I"],
                    ["I", "I", "I", "I"],
                    ["I", "I", "I", "I"],
                    ["I", "I", "I", "I"],
                    ["I", "I", "I", "I"]]
question = 0
count = 0
question_content = [
            ["A. Expend energy, enjoy groups.", "B. Conserve energy, one-on-one"],
            ["A. Interpret literally.", "B. Look for meaning and possibilities."],
            ["A. Logical, thinking, questioning.", "B. Empathetic, feeling, accommodating"],
            ["A. Organized, orderly.", "B. Flexible, adaptable"],
            ["A. More outgoing, think out loud.", "B. More reserved, think to yourself."],
            ["A. Practical, realistic, experiential.", "B. Imagination, innovative, theoretical."],
            ["A. Candid, straight forward, frank.", "B. Tactful, kind, encouraging."],
            ["A. Plan, schedule.", "B. Unplanned, spontaneous"],
            ["A. seek many tasks, public activities, interaction with others",
            "B. seek private, solitary activities with quiet to concentrate."],
            ["A. Standard, usual, conventional.", " B. different, novel, unique."],
            ["A. Firm, tend to criticize, hold the line.", "B. gentle, tend to appreciate, conciliate."],
            ["A. Regulated, structured.", " B. easygoing, live  and let live"],
            ["A. External, communicative, express yourself.", "B. internal, reticent, keep to yourself."],
            ["A. Focus on here-and-now.", " B. look to the future, global perspective, 'big picture'"],
            ["A. Tough minded, just.", "B. tender-hearted, merciful"],
            ["A. Preparation, plan ahead.", "B. go with the flow, adapt as you go."],
            ["A. Active, initiate.", "B. reflective, deliberate"],
            ["A. Facts, things, what is", "B. ideas, dreams, what could be, philosophical"],
            ["A. Matter of fact, issue oriented.", "B. sensitive, people-oriented, compassionate"],
            ["A. Control, govern", "B. latitude, freedom"]
                ]

e_icounter_a = 0
e_icounter_b = 0
s_ncounter_a = 0
s_ncounter_b = 0
t_fcounter_a = 0
t_fcounter_b = 0
j_pcounter_a = 0
j_pcounter_b = 0

collation = ""
name = ""

def name_collector() -> None:
    global name
    user_name = input("What is your name: ")
    if re.fullmatch('[A-Za-z]{2,25}\s[A-Za-z]{2,25}', user_name):
        name = user_name
    else:
        print("Invalid Entry, Try Again!!. A name should contain only Letters from A to Z")
        name_collector()


user_response = ""

def saved_questions() -> None:
    global e_icounter_a, e_icounter_b, user_response

    user_response = input()
    if user_response.capitalize() in ["A", "B"]:
        match question:
            case 1:
                if user_response.upper() == "A":
                    all_user_entries[0][0] = question_content[0][0]
                    e_icounter_a +=1
                else:
                    all_user_entries[0][0] = question_content[0][1]
                    e_icounter_b +=1
            case 5:
                if user_response.upper() == "A":
                    all_user_entries[1][0] = question_content[4][0]
                    e_icounter_a+=1
                else:
                    all_user_entries[1][0] = question_content[4][1]
                    e_icounter_b+=1
            case 9:
                if user_response.upper() == "A":
                    all_user_entries[2][0] = question_content[8][0]
                    e_icounter_a+=1
                else:
                    all_user_entries[2][0] = question_content[8][1]
                    e_icounter_b+=1
            case 13:
                if user_response.upper() == "A":
                    all_user_entries[3][0] = question_content[12][0]
                    e_icounter_a+=1
                else:
                    all_user_entries[3][0] = question_content[12][1]
                    e_icounter_b+=1

            case 17:
                if user_response.upper() == "A":
                    all_user_entries[4][0] = question_content[16][0]
                    e_icounter_a+=1
                else :
                    all_user_entries[4][0] = question_content[16][1]
                    e_icounter_b+=1
        second_segement()
    else:
        print("Expected A or B as response.\nI know this is an error, Please Try again!")
        all_questions()
        saved_questions()
def second_segement():
    global s_ncounter_a, s_ncounter_b, user_response
    match question:
        case 2:
            if user_response.upper() == "A":
                all_user_entries[0][1] = question_content[1][0]
                s_ncounter_a+=1
            else:
                all_user_entries[0][1] = question_content[1][1]
                s_ncounter_b+=1
        case 6:
            if user_response.upper() == "A":
                all_user_entries[1][1] = question_content[5][0]
                s_ncounter_a+=1
            else :
                all_user_entries[1][1] = question_content[5][1]
                s_ncounter_b+=1
        case 10:
            if user_response.upper() == "A":
                all_user_entries[2][1] = question_content[9][0]
                s_ncounter_a+=1
            else:
                all_user_entries[2][1] = question_content[9][1]
                s_ncounter_b+=1
        case 14:
            if user_response.upper() == "A":
                all_user_entries[3][1] = question_content[13][0]
                s_ncounter_a+=1
            else:
                all_user_entries[3][1] = question_content[13][1]
                s_ncounter_b+=1
        case 18:
            if user_response.upper() == "A":
                all_user_entries[4][1] = question_content[17][0]
                s_ncounter_a+=1
            else:
                all_user_entries[4][1] = question_content[17][1]
                s_ncounter_b+=1
    third_segment()
def third_segment():
    global t_fcounter_a, t_fcounter_b, user_response
    match question:
        case 3:
            if user_response.upper() == "A":
                all_user_entries[0][2] = question_content[2][0]
                t_fcounter_a+=1
            else:
                all_user_entries[0][2] = question_content[2][1]
                t_fcounter_b+=1

        case 7:
            if user_response.upper() == "A":
                all_user_entries[1][2] = question_content[6][0]
                t_fcounter_a+=1
            else:
                all_user_entries[1][2] = question_content[6][1]
                t_fcounter_b+=1

        case 11:
            if user_response.upper() == "A":
                all_user_entries[2][2] = question_content[10][0]
                t_fcounter_a+=1
            else :
                all_user_entries[2][2] = question_content[10][1]
                t_fcounter_b+=1
        case 15:
            if user_response.upper() == "A":
                all_user_entries[3][2] = question_content[14][0]
                t_fcounter_a+=1
            else:
                all_user_entries[3][2] = question_content[14][1]
                t_fcounter_b+=1

        case 19:
            if user_response.upper() == "A":
                all_user_entries[4][2] = question_content[18][0]
                t_fcounter_a+=1
            else:
                all_user_entries[4][2] = question_content[18][1]
                t_fcounter_b+=1
    fourth_segment()
def fourth_segment():
    global j_pcounter_a, j_pcounter_b, user_response

    match question:
        case 4:
            if user_response.upper() == "A":
                all_user_entries[0][3] = question_content[3][0]
                j_pcounter_a+=1
            else:
                all_user_entries[0][3] = question_content[3][1]
                j_pcounter_b+=1

        case 8:
            if user_response.upper() == "A":
                all_user_entries[1][3] = question_content[7][0]
                j_pcounter_a+=1
            else:
                all_user_entries[1][3] = question_content[7][1]
                j_pcounter_b+=1

        case 12:
            if user_response.upper() == "A":
                all_user_entries[2][3] = question_content[11][0]
                j_pcounter_a+=1
            else:
                all_user_entries[2][3] = question_content[11][1]
                j_pcounter_b+=1

        case 16:
            if user_response.upper() == "A":
                all_user_entries[3][3] = question_content[15][0]
                j_pcounter_a+=1
            else:
                all_user_entries[3][3] = question_content[15][1]
                j_pcounter_b+=1

        case 20:
            if user_response.upper() == "A":
                all_user_entries[4][3] = question_content[19][0]
                j_pcounter_a+=1
            else:
                all_user_entries[4][3] = question_content[19][1]
                j_pcounter_b+=1

    question_generator()
    all_questions()
    saved_questions()

def question_generator():
    global question, count
    if count < 20:
        count += 1
        question = count
    else:
        responses_collation()


def all_questions() -> None:
    global question_content

    match question:
        case 1:
            print(question_content[0][0], "  ", question_content[0][1])
        case 2:
            print(question_content[1][0], "  ", question_content[1][1])
        case 3:
            print(question_content[2][0], "  ", question_content[2][1])
        case 4:
            print(question_content[3][0], "  ", question_content[3][1])
        case 5:
            print(question_content[4][0], "  ", question_content[4][1])
        case 6:
            print(question_content[5][0], "  ", question_content[5][1])
        case 7:
            print(question_content[6][0], "  ", question_content[6][1])
        case 8:
            print(question_content[7][0], "  ", question_content[7][1])
        case 9:
            print(question_content[8][0], "  ", question_content[8][1])
        case 10:
            print(question_content[9][0], "  ", question_content[9][1])
        case 11:
            print(question_content[10][0], "  ", question_content[10][1])
        case 12:
            print(question_content[11][0], "  ", question_content[11][1])
        case 13:
            print(question_content[12][0], "  ", question_content[12][1])
        case 14:
            print(question_content[13][0], "  ", question_content[13][1])
        case 15:
            print(question_content[14][0], "  ", question_content[14][1])
        case 16:
            print(question_content[15][0], "  ", question_content[15][1])
        case 17:
            print(question_content[16][0], "  ", question_content[16][1])
        case 18:
            print(question_content[17][0], "  ", question_content[17][1])
        case 19:
            print(question_content[18][0], "  ", question_content[18][1])
        case 20:
            print(question_content[19][0], "  ", question_content[19][1])

def responses_collation() -> None:
    global collation
    collation += "E" if (e_icounter_a > e_icounter_b) else "I"
    collation += "S" if (s_ncounter_a > s_ncounter_b) else "N"
    collation += "T" if (t_fcounter_a > t_fcounter_b) else "F"
    collation += "J" if (j_pcounter_a > j_pcounter_b) else "P"
    check_personality()


def check_personality() -> None:
    global e_icounter_a, e_icounter_b,s_ncounter_a, s_ncounter_b, t_fcounter_a, t_fcounter_b, j_pcounter_a, j_pcounter_b

    print(f"Hello  {name}  You selected")
    print(all_user_entries[0][0], "\n",all_user_entries[1][0], "\n",all_user_entries[2][0], "\n",all_user_entries[3][0],
          "\n",all_user_entries[4][0], "\nNumber of A selected =  ", e_icounter_a,
          "\nNumber of B selected =  ", e_icounter_b)
    print()
    print(all_user_entries[0][1], "\n",all_user_entries[1][1],"\n",all_user_entries[2][1],
          "\n",all_user_entries[3][1], "\n",all_user_entries[4][1],
          "\n", "Number of A selected =  ", s_ncounter_a, "\nNumber of B selected = ", s_ncounter_b)
    print()
    print(all_user_entries[0][2], "\n",all_user_entries[1][2], "\n",
          all_user_entries[2][2], "\n",all_user_entries[3][2], "\n",all_user_entries[4][2],
          "\nNumber of A selected =  ", t_fcounter_a, "\nNumber of B selected = ", t_fcounter_b)
    print()
    print(all_user_entries[0][3], "\n",all_user_entries[1][3], "\n",
          all_user_entries[2][3], "\n",all_user_entries[3][3], "\n",all_user_entries[4][3],
          "\nNumber of A selected =  ", j_pcounter_a, "\nNumber of B selected = ", j_pcounter_b)

    print(f"\nYour personality is: {collation}")
    display_output()

def display_output() -> None:
    global collation
    match collation:
        case "ESTP":
            print("""
                An ESTP personalities
                ESTP is someone with the Extraverted, Observant, Thinking, and Prospecting personality traits. 
                They tend to be energetic and action-oriented, deftly navigating whatever is in front of them.

                They love uncovering life’s opportunities, whether socializing with others or in more personal pursuits.
                ESTPs always have an impact on their immediate surroundings – 
                the best way to spot them at a party is to look for the whirling eddy of people flitting about 
                them as they move from group to group. Laughing and entertaining with a blunt and earthy humor, 
                ESTP personalities love to be the center of attention. If an audience member is 
                asked to come on stage, ESTPs volunteer – or volunteer a shy friend.

                Theory, abstract concepts and plodding discussions about global issues and their 
                implications don’t keep ESTPs interested for long. ESTPs keep their conversation energetic, 
                with a good dose of intelligence, but they like to talk about what is – or better yet, 
                to just go out and do it. ESTPs leap before they look, fixing their mistakes as they go, 
                rather than sitting idle, preparing contingencies and escape clauses.

                ESTPs are the likeliest personality type to make a lifestyle of risky behavior. 
                They live in the moment and dive into the action – they are the eye of the storm. 

                People with the ESTP personality type enjoy drama, passion, and pleasure, not for emotional 
                thrills, but because it’s so stimulating to their logical minds. They are forced to make 
                critical decisions based on factual, immediate reality in a process of rapid-fire 
                rational stimulus response.""")
            exit()
        case "ESTJ":
            print("""
                ESTJ
                An ESTJ (ESTJ) is someone with the Extraverted, Observant, Thinking, and 
                Judging personality traits. They possess great fortitude, emphatically following their 
                own sensible judgment. They often serve as a stabilizing force among others, 
                able to offer solid direction amid adversity.

                ESTJs are representatives of tradition and order, utilizing their understanding of 
                what is right, wrong and socially acceptable to bring families and communities together. 
                Embracing the values of honesty, dedication and dignity, people with the ESTJ personality type 
                are valued for their clear advice and guidance, and they happily lead the way on difficult paths. 
                Taking pride in bringing people together, ESTJs often take on roles as community organizers, 
                working hard to bring everyone together in celebration of cherished local events, 
                or in defense of the traditional values that hold families and communities together.
                ESTJ personality

                Demand for such leadership is high in democratic societies, and forming no less than 11% of 
                the population, it’s no wonder that many of America’s presidents have been ESTJs. 
                Strong believers in the rule of law and authority that must be earned, ESTJ personalities 
                lead by example, demonstrating dedication and purposeful honesty, and an utter rejection of 
                laziness and cheating, especially in work. If anyone declares hard, manual work to be an 
                excellent way to build character, it is ESTJs.

                ESTJs are aware of their surroundings and live in a world of clear, verifiable facts – 
                the surety of their knowledge means that even against heavy resistance, they stick to their 
                principles and push an unclouded vision of what is and is not acceptable. Their opinions 
                aren’t just empty talk either, as ESTJs are more than willing to dive into the most 
                challenging projects, improving action plans and sorting details along the way, 
                making even the most complicated tasks seem easy and approachable.

                However, ESTJs don’t work alone, and they expect their reliability and work ethic to be 
                reciprocated – people with this personality type meet their promises, and if partners or 
                subordinates jeopardize them through incompetence or laziness, or worse still, dishonesty, 
                they do not hesitate to show their wrath. This can earn them a reputation for inflexibility, 
                a trait shared by all Sentinel personalities, but it’s not because ESTJs are arbitrarily 
                stubborn, but because they truly believe that these values are what make society work.""")
            exit()

        case "ESFJ":
            print("""
                An ESFJ Personalities
                A ESFJ (ESFJ) is a person with the Extraverted, Observant, Feeling, and Judging personality 
                traits. They are attentive and people-focused, and they enjoy taking part in their social 
                community. Their achievements are guided by decisive values, and they willingly offer guidance to others.
                Encourage, lift, and strengthen one another. For the positive energy spread to one will be felt by us all.
                For ESFJs, life is sweetest when it’s shared with others. People with this personality 
                type form the bedrock of many communities, opening their homes – and their hearts – 
                to friends, loved ones, and neighbors.

                This doesn’t mean that ESFJs like everyone, or that they’re saints. But ESFJs do believe 
                in the power of hospitality and good manners, and they tend to feel a sense of duty to 
                those around them. Generous and reliable, people with this personality type often take it 
                upon themselves – in ways both large and small – to hold their families and their communities together.

                ESFJs have a talent for making the people in their lives feel supported, cared for, and secure.
                ESFJs are altruists. They take seriously their responsibilities to give back, serve others, 
                and do the right thing.

                And ESFJs believe that there is a clear right thing to do in nearly every situation. 
                While some personality types adopt a more lenient, live-and-let-live attitude, ESFJs may find 
                it difficult not to judge when someone takes a path that strikes them as misguided. As a result, 
                ESFJs often struggle to accept it when someone – particularly someone they care about – disagrees with them.

                ESFJs have a clear moral compass – and it can be nothing short of baffling to them 
                when other people’s actions don’t align with it.
                With their definite views on right and wrong, ESFJs tend to be on the opinionated side. 
                But these opinions aren’t arbitrary – they’re often based on a deep respect for tradition. 
                ESFJs know that everything they do affects someone else, and they trust that established laws, 
                protocols, and social norms will help them navigate their everyday lives in a way 
                that is considerate and responsible toward others.""")
            exit()
        case "ESFP":
            print("""
                An ESFP Personalities
                ESFP is a person with the Extraverted, Observant, Feeling, and Prospecting personality traits. 
                These people love vibrant experiences, engaging in life eagerly and taking pleasure in 
                discovering the unknown. They can be very social, often encouraging others 
                into shared activities.

                If anyone is to be found spontaneously breaking into song and dance, it is the ESFP 
                personality type. ESFPs get caught up in the excitement of the moment, and want everyone 
                else to feel that way, too. No other personality type is as generous with their time and energy 
                as ESFPs when it comes to encouraging others, and no other personality type does 
                it with such irresistible style.

                ESFPs love the spotlight, and all the world’s a stage. Many famous people with the 
                ESFP personality type are indeed actors, but they love putting on a show for their friends too,
                chatting with a unique and earthy wit, soaking up attention and making every outing feel a 
                bit like a party. Utterly social, ESFPs enjoy the simplest things, and there’s no greater 
                joy for them than just having fun with a good group of friends.

                It’s not just talk either – ESFPs have the strongest aesthetic sense of any personality type. 
                From grooming and outfits to a well-appointed home, ESFP personalities have an eye for fashion. 
                Knowing what’s attractive the moment they see it, ESFPs aren’t afraid to change their 
                surroundings to reflect their personal style. ESFPs are naturally curious, exploring 
                new designs and styles with ease.

                Though it may not always seem like it, ESFPs know that it’s not all about them – 
                they are observant, and very sensitive to others’ emotions. People with this personality 
                type are often the first to help someone talk out a challenging problem, happily providing 
                emotional support and practical advice. However, if the problem is about them, ESFPs are more 
                likely to avoid a conflict altogether than to address it head-on. ESFPs usually love a little 
                drama and passion, but not so much when they are the focus of the criticisms it can bring.""")
            exit()

        case "ENTJ":
            print("""
                An ENTJ personalities
                A (ENTJ) is someone with the Extraverted, Intuitive, Thinking, and Judging personality traits.
                They are decisive people who love momentum and accomplishment. 
                They gather information to construct their creative visions but rarely 
                hesitate for long before acting on them.

                If there’s anything ENTJs love,it’s a good challenge, big or small, and 
                they firmly believe that given enough time and resources, they can achieve any goal. 
                This quality makes people with the Commander personality type brilliant entrepreneurs, 
                and their ability to think strategically and hold a long-term focus while executing each step of 
                their plans with determination and precision makes them powerful business leaders.

                ENTJs see inefficiency not just as a problem in its own right, but as something that pulls time 
                and energy away from all their future goals, an elaborate sabotage consisting of 
                irrationality and laziness. People with the ENTJ personality type will 
                root out such behavior wherever they go.

                Energetic – Rather than finding this process taxing ENTJ are energized by it, 
                genuinely enjoying leading their teams forward as they implement their plans and goals.
                ENTJ couldn’t do this if they were plagued by self-doubt – they trust their abilities, 
                make known their opinions, and believe in their capacities as leaders.
                Strong-Willed – Nor do they give up when the going gets tough – Commander personalities strive 
                to achieve their goals, but really nothing is quite as satisfying to them as rising to 
                the challenge of each obstacle in their run to the finish line.

                ENTJ exemplify the difference between moment-to-moment crisis management and navigating 
                the challenges and steps of a bigger plan, and are known for examining every angle of a 
                problem and not just resolving momentary issues, but moving the whole project forward 
                with their solutions. These qualities combine to create individuals who are able to inspire 
                and invigorate others, who people actually want to be their leaders, and this in turn helps 
                Commanders to accomplish their often ambitious goals that could never be finished alone.
                """)
            exit()

        case "ENTP":
            print("""
                ENTP personalities
                An (ENTP) is a person with the Extraverted, Intuitive, Thinking, and 
                Prospecting personality traits. They tend to be bold and creative, deconstructing and 
                rebuilding ideas with great mental agility. They pursue their goals vigorously 
                despite any resistance they might encounter.
                Quick-witted and audacious, ENTP aren’t afraid to disagree with the status quo. 
                In fact, they’re not afraid to disagree with pretty much anything or anyone. 
                Few things light up people with this personality type more than a bit of verbal sparring – 
                and if the conversation veers into controversial terrain, so much the better.

                ENTP are known for their rebellious streak. For this personality type, no belief is too 
                sacred to be questioned, no idea is too fundamental to be scrutinized, and no rule is too 
                important to be broken, or at least thoroughly tested. Sometimes ENTP even rebel against their 
                own beliefs by arguing the opposing viewpoint – just to see how the 
                world looks from the other side.

                some of the weakness of the ENTP are that they have mental exercise of debating and to them, 
                nothing is sacred. They often misjudge others feelings and push their debtates well past others 
                tolerance level. sometimes this personalities find it difficult to focus.
                some of the Strength of this personality is that hey are very knowledgeable, they are quick 
                thinkers, and excellent brainstormers. Their confidence, quick thought and ability to connect 
                disparate ideas in novel ways create a style of communication that is charming, 
                even entertaining, and informative at the same time.""")
            exit()

        case "ENFP":
            print("""
                A ENFP (ENFP) is someone with the Extraverted, Intuitive, Feeling, 
                and Prospecting personality traits. 
                These people tend to embrace big ideas and actions that reflect their sense of hope 
                and goodwill toward others. Their vibrant energy can flow in many directions.

                ENFPs (ENFPs) are true free spirits – outgoing, openhearted, and open-minded. 
                With their lively, upbeat approach to life, they stand out in any crowd. 
                But even though they can be the life of the party, ENFPs don’t just care about having a good time. 
                These personality types run deep – as does their longing for meaningful, 
                emotional connections with other people.

                Friendly and outgoing, ENFPs are devoted to enriching their relationships and 
                their social lives. But beneath their sociable, easygoing exteriors, 
                they have rich, vibrant inner lives as well. 

                Without a healthy dose of imagination, creativity, and curiosity, an ENFP simply wouldn’t be a ENFP.
                In their unique way, ENFPs can be quite introspective. They can’t help 
                but ponder the deeper meaning and significance of life – even when they should be paying 
                attention to something else. These personalities believe that everything – 
                and everyone – is connected, and they live for the glimmers of insight that 
                they can gain into these connections.""")
            exit()

        case "ENFJ":
            print("""
                An ENFJ personalities
                A ENTJ is a person with the Extraverted, Intuitive, Feeling, and Judging personality traits.
                These warm, forthright types love helping others, and they tend to have strong ideas and values.
                They back their perspective with the creative energy to achieve their goals.
                ENTJs (ENFJs) feel called to serve a greater purpose in life.

                Thoughtful and idealistic, these personality types strive to have a positive
                impact on other people and the world around them.
                They rarely shy away from an opportunity to do the right thing,
                even when doing so is far from easy.

                ENTJs are born leaders, which explains why these personalities can be found
                among many notable politicians, coaches, and teachers.
                Their passion and charisma allow them to inspire others not just in their careers
                but in every arena of their lives, including their relationships. 
                Few things bring ENTJs a deeper sense of joy and fulfillment than guiding friends and 
                loved ones to grow into their best selves.

                ENTJs tend to be vocal about their values, including authenticity and altruism. 
                When something strikes them as unjust or wrong, they speak up. 
                But they rarely come across as brash or pushy, as their sensitivity and insight guide 
                them to speak in ways that resonate with others.

                People with this personality type are devoted altruists, ready to face slings and 
                arrows in order to stand up for the people and ideas that they believe in. 
                This strength of conviction bolsters ENTJs’ innate leadership skills, 
                particularly their ability to guide people to work together in service of the greater good.""")
            exit()

        case "ISTP":
            print("""
                An ISTP personalities
                ISTP is someone with the Introverted, Observant, Thinking, and Prospecting personality traits. 
                They tend to have an individualistic mindset, pursuing goals without needing much external 
                connection. They engage in life with inquisitiveness and personal skill, varying their approach as needed.
                ISTPs love to explore with their hands and their eyes, touching and examining the world around 
                them with cool rationalism and spirited curiosity. People with this personality type are 
                natural Makers, moving from project to project, building the useful and the superfluous for 
                the fun of it, and learning from their environment as they go. Often mechanics and engineers, 
                ISTPs find no greater joy than in getting their hands dirty pulling things apart and putting 
                them back together, just a little bit better than they were before.

                ISTPs explore ideas through creating, troubleshooting, trial and error and first-hand experience. 
                They enjoy having other people take an interest in their projects and sometimes don’t even 
                mind them getting into their space. Of course, that’s on the condition that those people don’t 
                interfere with ISTPs’ principles and freedom, and they’ll need to be open to ISTPs 
                returning the interest in kind.

                ISTPs enjoy lending a hand and sharing their experience, especially with the people they care 
                about, and it’s a shame they’re so uncommon, making up only about five percent of the 
                population. ISTP women are especially rare, and the typical gender roles that society tends to 
                expect can be a poor fit – they’ll often be seen as tomboys from a young age.""")
            exit()

        case "ISTJ":
            print("""
                An ISTJ Personalities
                A Logistician (ISTJ) is someone with the Introverted, Observant, Thinking, and Judging
                personality traits. These people tend to be reserved yet willful, with a rational outlook 
                on life. They compose their actions carefully and carry them out with methodical purpose.
                ISTJ pride themselves on their integrity. People with this personality type mean what they 
                say, and when they commit to doing something, they make sure to follow through.

                This personality type makes up a good portion of the overall population, and while 
                ISTJ may not be particularly flashy or attention-seeking, they do more than their share to keep 
                society on a sturdy, stable foundation. In their families and their communities, ISTJ often 
                earn respect for their reliability, their practicality, and their ability to stay grounded 
                and logical, even in the most stressful situations.

                The core of ISTJ’ self-respect comes from a sense of personal integrity. People with this 
                personality type believe that there is a right way to proceed in any situation – and that 
                anyone who pretends otherwise is probably trying to bend the rules to suit their own purposes. 
                ISTJ have a deep respect for structure and tradition, and they are often drawn to organizations,
                 workplaces, and educational settings that offer clear hierarchies and expectations.

                For many ISTJ, a lack of structure offers not freedom, but chaos.
                People with the Logistician personality type rarely hesitate to take responsibility for 
                their actions and choices. Generally speaking, they are quick to own up to their own mistakes, 
                admitting the truth even if it doesn’t make them look good. To ISTJ, honesty is far more 
                important than showmanship, and they’d rather satisfy their own conscience than 
                lie to impress someone else.

                ISTJ’ dedication is an admirable quality, and it drives many of their accomplishments. 
                But it can also become a weakness that other people take advantage of. With their strong work 
                ethic and sense of duty, ISTJ may routinely find themselves shouldering other people’s 
                responsibilities. Even if they don’t complain about the situation, ISTJ can end up exhausted 
                or discouraged if they’re constantly expected – or taking it upon themselves – to pick up 
                the slack for their colleagues, friends, or loved ones.""")
            exit()

        case "ISFJ":
            print("""
                ISFJ
                A ISFJ is someone with the Introverted, Observant, Feeling, and Judging personality traits. 
                These people tend to be warm and unassuming in their own steady way. They’re efficient and 
                responsible, giving careful attention to practical details in their daily lives.

                In their unassuming, understated way, ISFJs help make the world go round. Hardworking and 
                devoted, people with this personality type feel a deep sense of responsibility to those 
                around them. ISFJs can be counted on to meet deadlines, remember birthdays and special 
                occasions, uphold traditions, and shower their loved ones with gestures of care and support. 
                But they rarely demand recognition for all that they do, preferring instead to 
                operate behind the scenes.

                This is a capable, can-do personality type, with a wealth of versatile gifts. 
                Though sensitive and caring, ISFJs also have excellent analytical abilities and an eye for 
                detail. And despite their reserve, they tend to have well-developed people skills and 
                robust social relationships. ISFJs are truly more than the sum of their parts, and their 
                varied strengths shine in even the most ordinary aspects of their daily lives.
                ISFJs are true altruists, meeting kindness with kindness-in-excess and engaging with 
                the work and people they believe in with enthusiasm and generosity.

                The Gift of Loyalty
                Among ISFJs’ most distinctive traits is loyalty. Rare is the ISFJ who allows a friendship or 
                relationship to fade away from lack of effort. Instead, they invest a great deal of energy into 
                maintaining strong connections with their loved ones – and not just by sending 
                “How are you doing?” texts. People with this personality type are known for dropping everything 
                and lending a hand whenever a friend or family member is going through a hard time.
                ISFJs tend to feel most energized and effective when they’re showing up for 
                someone who needs their help.""")
            exit()

        case "ISFP":
            print("""
                An ISFP Personality Type
                An ISFP is a person with the Introverted, Observant, Feeling, and Prospecting 
                personality traits. They tend to have open minds, approaching life, new experiences, 
                and people with grounded warmth. Their ability to stay in the moment helps them uncover 
                exciting potentials.

                ISFPs are true artists – although not necessarily in the conventional sense. For this 
                personality type, life itself is a canvas for self-expression. From what they wear to how they 
                spend their free time, ISFPs act in ways that vividly reflect who they are as unique individuals.
                And every ISFP is certainly unique. Driven by curiosity and eager to try new things, people 
                with this personality often have a fascinating array of passions and interests. With their 
                exploratory spirits and their ability to find joy in everyday life, ISFPs can be among the most 
                interesting people you’ll ever meet. The only irony? Unassuming and humble, ISFPs tend to see 
                themselves as “just doing their own thing,” so they may not even realize how remarkable 
                they really are.

                ISFPs embrace a flexible, adaptable approach to life. Some personality types thrive on 
                strict schedules and routines – but not ISFPs. ISFPs take each day as it comes, doing what 
                feels right to them in the moment. And they make sure to leave plenty of room in their lives 
                for the unexpected – with the result that many of their most cherished memories are of 
                spontaneous, spur-of-the-moment outings and adventures, whether by themselves 
                or with their loved ones.

                This flexible mindset makes ISFPs remarkably tolerant and open-minded. 
                These personalities genuinely love living in a world filled with all kinds of people 
                – even people who disagree with them or choose radically different lifestyles. It’s no 
                surprise, then, that ISFPs are unusually open to changing their minds and rethinking their 
                opinions. If any personality type believes in giving something (or someone) a second chance, 
                it’s ISFPs.

                ISFPs want to live in a world where they – and everyone else – have the freedom to live as 
                they see fit, without judgment.
                That said, ISFPs’ go-with-the-flow mentality can have its downsides. People with this 
                personality type may struggle to set long-term plans – let alone stick with them. 
                As a result, ISFPs tend to have a pretty cloudy view of their ability to achieve their goals, 
                and they often worry about letting other people down. ISFPs may find that adding a little 
                structure to their lives goes a long way toward helping them feel more capable and 
                organized – without quashing their independent spirits.""")
            exit()

        case "INTJ":
            print("""
                An INTJ personality type
                An INTJ is a person with the Introverted, Intuitive, Thinking, and Judging personality traits.
                These thoughtful tacticians love perfecting the details of life, applying creativity and 
                rationality to everything they do. Their inner world is often a private, complex one.
                Rational and quick-witted, INTJs pride themselves on their ability to think for themselves, 
                not to mention their uncanny knack for seeing right through phoniness and hypocrisy. But because 
                their minds are never at rest, Architects may struggle to find people who can keep up with 
                their nonstop analysis of everything around them.

                This personality type comes with a strong independent streak. INTJs don’t mind acting alone, 
                perhaps because they don’t like waiting around for others to catch up with them. They also 
                generally prefer making decisions without asking for anyone else’s input. At times, this 
                lone-wolf behavior can come across as insensitive, as it fails to take into consideration 
                other people’s thoughts, desires, and plans.

                Architects contemplate the strengths and weaknesses of each move before they make it. 
                And they never lose faith that, with enough ingenuity and insight, they can find a way to 
                win – no matter what challenges might arise along the way.

                INTJ personalities can be rational, informed, independent, determined curious, and original. 
                And some are their weaknesses is that they are arogant, dismissive of  emotions, 
                Overly Critical, Combative, Socially Clueless.""")
            exit()

        case "INTP":
            print("""
                An INTP personality Type
                A (INTP) is someone with the Introverted, Intuitive, Thinking, and Prospecting personality 
                traits. These flexible thinkers enjoy taking an unconventional approach to many aspects of life. 
                They often seek out unlikely paths, mixing willingness to experiment with personal creativity.
                INTP often lose themselves in thought – which isn’t necessarily a bad thing. People with this 
                personality type hardly ever stop thinking. From the moment they wake up, their minds buzz with 
                ideas, questions, and insights. At times, they may even find themselves conducting full-fledged 
                debates in their own heads.

                People with this personality type want to understand everything in the universe, but one area 
                in particular tends to mystify them: human nature. As their name suggests, Logicians feel most 
                at home in the realm of logic and rationality. As a result, they can find themselves baffled 
                by the illogical, irrational ways that feelings and emotions influence people’s behavior – 
                including their own.

                Some of this personality strength is that they analyze everything that they come across, 
                from research data to the behavior of the people around them. Thanks to their unrelenting 
                imagination, Logicians can come up with creative, counterintuitive ideas that wouldn’t 
                occur to most people. Logicians are driven by curiosity and an intense desire to learn 
                everything that they can. These personalities are always casting about for new pursuits, 
                hobbies, and areas of research. they care about the truth. Rather than taking comfort in 
                ideology or received ideas, they want to understand what’s really going on beneath the 
                surface of things.""")
            exit()
        case "INFP":
            print("""
                An INFP Personality Type
                A INFP is someone who possesses the Introverted, Intuitive, Feeling, and Prospecting
                personality traits. These rare personality types tend to be quiet, open-minded, and 
                imaginative, and they apply a caring and creative approach to everything they do.
    
                Although they may seem quiet or unassuming,  (INFPs) have vibrant, passionate inner lives. 
                Creative and imaginative, they happily lose themselves in daydreams, inventing all sorts of 
                stories and conversations in their minds. These personalities are known for their sensitivity. 
                INFP can have profound emotional responses to music, art, nature, and the people around them.
    
                Idealistic and empathetic, INFP long for deep, soulful relationships, and they feel called to 
                help others. But because this personality type makes up such a small portion of the population,
                 INFPs may sometimes feel lonely or invisible, adrift in a world that doesn’t seem to 
                 appreciate the traits that make them unique.
    
                Empathy is among this personality type’s greatest gifts, but at times it can be a liability. 
                The troubles of the world weigh heavily on INFP’ shoulders, and these personalities can be 
                vulnerable to internalizing other people’s negative moods or mindsets. Unless they learn to 
                set boundaries, INFP may feel overwhelmed by just how many wrongs there are 
                that need to be set right.
    
                People with this personality type tend to feel directionless or stuck until they connect 
                with a sense of purpose for their lives. For many INFP, this purpose has something to do with 
                uplifting others and their ability to feel other people’s suffering as if it were their own. 
                While INFP want to help everyone, they need to focus their energy and efforts – 
                otherwise, they can end up exhausted.""")
            exit()

        case "INFJ":
            print("""
                An INFJ Personality Type
                An (INFJ) is someone with the Introverted, Intuitive, Feeling, and Judging personality
                 traits. They tend to approach life with deep thoughtfulness and imagination. 
                 Their inner vision, personal values, and a quiet, principled version of humanism 
                 guide them in all things.

                “Treat people as if they were what they ought to be and you help them to become what 
                they are capable of being.”

                (INFJs) may be the rarest personality type of all, but they certainly leave their mark on 
                the world. Idealistic and principled, they aren’t content to coast through life – they want 
                to stand up and make a difference. For Advocate personalities, success doesn’t come 
                from money or status but from seeking fulfillment, helping others, and being a force 
                for good in the world.

                While they have lofty goals and ambitions, INFJs shouldn’t be mistaken for idle dreamers. 
                People with this personality type care about integrity, and they’re rarely satisfied until 
                they’ve done what they know to be right. Conscientious to the core, they move through life 
                with a clear sense of their values, and they aim never to lose sight of what truly matters – 
                not according to other people or society at large, but according to their own wisdom and intuition.

                Perhaps because their personality type is so uncommon, INFJs tend to carry around a sense – 
                whether conscious or not – of being different from most people. With their rich inner lives 
                and their deep, abiding desire to find their life purpose, they don’t always fit in with those 
                around them. This isn’t to say that Advocates can’t enjoy social acceptance or close 
                relationships – only that they sometimes feel misunderstood or at odds with the world.

                INFJ may be Introverted, but they value deep, authentic relationships with others. 
                Few things bring these personalities as much joy as truly knowing another person – and 
                being known in return. Advocates enjoy meaningful conversations far more than small talk, 
                and they tend to communicate in a way that is warm and sensitive""")
            exit()

if __name__ == '__main__':
    name_collector()
    question_generator()
    all_questions()
    saved_questions()