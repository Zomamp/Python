from llm_sdk import Small_LLM_Model
import json


if __name__ == "__main__":
    try:

        # Debut de mon petit llm
        # instance de la class

        src = Small_LLM_Model()
        # Mapiditra anle json
        with open("./data/input/functions_definition.json", "r") as file:
            data = json.load(file)

        # User request lesy zanjy ah
        with open("./prompt/prompt.json", "r") as dir:
            user_request  = json.load(dir)

        # # Bouclage de la liste de dictionnaire pour parcourir cette liste
        # for item in range(len(user)):
        #     user_request = user[item]

        # Test de boucle pour voir si la liste sera parcourue ou pas

        # Stockage pour rendu de JSON valide
        results = []
        with open("./output/output.json", "w") as output:
            output.write("")
        for i in user_request:

            prompts = i["prompt"]
            ex = '{"name": "fn_add_numbers","parameters": {"a": 2.0, "b": 3.0}, "result": {"resultat": 5.0} '
            # Add of the little prompt test
            prompt = f"""
            Your task is to select the appropriate function from the available functions
            and extract its arguments from the user's request.

            Available functions:
            {data}

            Example:
            User request: 'what's the sum of 2 and 3'
            Output: {ex}

            User request: {prompts}

            Output:
            """

            # encode ou tokenisation de chaque mot dans mon prompt
            token = src.encode(prompt)[0].tolist()
            # print(token)

            # Creation d'une petite boucle
            # deja_lu = []
            stockage = ""
            # decoder seulement si necessaire
            generated_token = []
            json_started = False
            print(f"\nPrompt: {i["prompt"]}")
            try:
                for _ in range(90):
                    # # Test de logit
                    logit = src.get_logits_from_input_ids(token)
                    # print(logit)

                    # scoring = logit.copy()
                    # Boucle hijerevana oe efa ao ve le token sa tsia raha efa ao dia apidinina le vecteur
                    # for efa_ao in deja_lu:
                    #     scoring[efa_ao] -= 2.0

                    # Choix du meilleur next token possible
                    next_best_token = max(range(len(logit)), key=logit.__getitem__)

                    # Ajout du nouveau token dans token variable
                    token.append(next_best_token)
                    # deja_lu.append(next_best_token)
                    # decode du next token car on veux pas de ID mais de mot
                    decodage_next = src.decode([next_best_token])
                    generated_token.append(next_best_token)

                    # On attend le premier {
                    if not json_started:
                        if "{" not in decodage_next:
                            continue

                        json_started = True

                    # print(next_best_token)
                    # Generation d prochain token baby
                    stockage += src.decode(next_best_token)
                    # print(decodage_next, end="", flush=True)
                    try:
                        result = json.loads(stockage)
                        results.append(result)
                        print(f"\n\033[034m{json.dumps(result, indent=2)}\033[0m")

                        # Ecris dans un fichier .json
                        with open("./output/output.json", "w") as output:
                            json.dump(results, output, indent=2)

                        break

                    except json.JSONDecodeError:
                        continue
        

            except KeyboardInterrupt as e:
                print("The program stop", e)


    except KeyboardInterrupt as e:
        print("The program stop", e)
