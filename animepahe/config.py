from Anime import Anime

# ^(\d+) +(.+\w|\d) +\w+ \d{1,2}, \d{4}$
# ^(.*)$
'''
{
        "resolution": "(720|360)",
        "audio": "(eng|jpn)",
        "disc": .*,
        "kwik": .*,
        "kwik_shst": .*,
        "kwik_adfly":.*"\n +},\n +
'''


'''
URL LIST

# For search
https://animepahe.ru/api?m=search&q=attack



'''

TEMPLATE = Anime("", "")
TEMPLATE = Anime("Shangri-La Frontier_ Kusoge Hunter, Kamige ni Idoman to su", "https://animepahe.ru/anime/c64b2f7c-7f17-3b6a-9733-8fe16de3adf2")
# TEMPLATE = Anime("Shingeki no Kyojin_ The Final Season Part 2", "https://animepahe.com/anime/7e9214f2-6d97-92f9-cb61-47967ff863ec")
# TEMPLATE = Anime("Beastars 2nd Season", "https://animepahe.com/anime/571ded38-5a95-ad41-f447-2ce6fa46623d")
# TEMPLATE = Anime("Beastars", "https://animepahe.com/anime/ae9208a8-910d-1032-4888-521c2d8193c8")
# TEMPLATE = Anime("Jujutsu Kaisen (TV)", "https://animepahe.com/anime/2e725010-900e-c5c8-6dde-4e9488ff1c0f")
# TEMPLATE = Anime("Shingeki no Kyojin_ The Final Season", "https://animepahe.com/anime/f751b966-3f43-60ab-dfee-3fa36ac1bd60")
# TEMPLATE = Anime("SK∞", "https://animepahe.com/anime/3eea35eb-c29f-f30d-b866-7cb5be9d583e")
# TEMPLATE = Anime("Yuukoku no Moriarty", "https://animepahe.com/anime/3e391206-145c-f867-d7e3-c19cb760a4f6")
# TEMPLATE = Anime("Araburu Kisetsu no Otome-domo yo", "https://animepahe.com/anime/4e675f24-81e1-18da-59c1-8379ff966c9d")
# TEMPLATE = Anime("Death Note", "https://animepahe.com/anime/ca9959e4-3380-fe90-0bbf-c0334e55a100")
# TEMPLATE = Anime("Boruto: Naruto Next Generations", "https://animepahe.com/anime/8b0eb1e8-8fb9-7e44-42a3-923eeb1c904c")
# TEMPLATE = Anime("Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka III", "https://animepahe.com/anime/fecf126a-7d06-262e-517a-98ea161b581b")
# TEMPLATE = Anime("Jujutsu Kaisen (TV)", "https://animepahe.com/anime/ba7da809-29b7-2766-c5c6-710a47a78d78")
# TEMPLATE = Anime("Mahouka Koukou no Rettousei: Raihousha-hen", "https://animepahe.com/anime/ee189387-976e-7aae-53d9-0a0e0575d707")
# TEMPLATE = Anime("Naruto", "https://animepahe.com/anime/b401cf63-c0da-6d82-b928-0fa894a723ca")
# TEMPLATE = Anime("Naruto: Shippuuden", "https://animepahe.com/anime/d6836058-7572-5f1d-87e8-e6135e3142ad")
# TEMPLATE = Anime("Naruto: Shippuuden Movie 5 - Blood Prison", "https://animepahe.com/anime/f02bf503-ef73-8a67-6d81-d49016b6ac07")
# TEMPLATE = Anime("Naruto: Shippuuden Movie 6 - Road to Ninja", "https://animepahe.com/anime/815fee96-8c5f-b45d-6ede-b139ff4412ac")
# TEMPLATE = Anime("Naruto: Shippuuden Movie 4 - The Lost Tower", "https://animepahe.com/anime/8aa3b53b-54dd-5bfb-645e-22d355e01d95")
# TEMPLATE = Anime("Naruto: Shippuuden Movie 2 - Kizuna", "https://animepahe.com/anime/cc4c5f9a-7568-bb95-273a-d2d3d566359b")
# TEMPLATE = Anime("Naruto: Shippuuden Movie 3 - Hi no Ishi wo Tsugu Mono", "https://animepahe.com/anime/5530c1ce-7ec5-fa8d-4dc5-6b9130155edf")
# TEMPLATE = Anime("Naruto: Shippuuden Movie 1", "https://animepahe.com/anime/0805a9d5-642c-d5c5-0c48-53f3aafc6a57")
# TEMPLATE = Anime("Naruto SD: Rock Lee no Seishun Full-Power Ninden", "https://animepahe.com/anime/9849975d-0d82-5b2d-1c90-311a73cdd634")
# TEMPLATE = Anime("Naruto Movie 3: Dai Koufun! Mikazuki Jima no Animaru Panikku Dattebayo!", "https://animepahe.com/anime/ea158d21-d8dd-82c2-c5e7-7ef5df4d3579")
# TEMPLATE = Anime("Naruto Movie 2: Dai Gekitotsu! Maboroshi no Chiteiiseki Dattebayo!", "https://animepahe.com/anime/6ec0f676-80f9-4516-95c5-b5ea1d35f6dd")
# TEMPLATE = Anime("Naruto Movie 1: Dai Katsugeki!! Yuki Hime Shinobu Houjou Dattebayo!", "https://animepahe.com/anime/700ba156-1df7-52c5-aac8-7423e2130158")
# TEMPLATE = Anime("Ore Monogatari!!", "https://animepahe.com/anime/73b73b42-e2b8-56b4-1832-96be740fa907")
# TEMPLATE = Anime("Shigatsu wa Kimi no Uso: Moments", "https://animepahe.com/anime/b63223cb-8761-9555-c354-8fbc68dc6a3f")
# TEMPLATE = Anime("Shigatsu wa Kimi no Uso", "https://animepahe.com/anime/a6b127e2-e314-08d7-d8b4-f51864e2bdae")
# TEMPLATE = Anime("Dragon Ball: Super Saiya-jin Zetsumetsu Keikaku", "https://animepahe.com/anime/5723fb8c-702b-e9c1-62d6-bb16ff453aea")
# TEMPLATE = Anime("Dragon Ball: Ossu! Kaettekita Son Gokuu to Nakama-tachi!!", "https://animepahe.com/anime/9af23b67-1b30-072f-c7cb-fd22e26498e9")
# TEMPLATE = Anime("Dragon Ball Z: Summer Vacation Special", "https://animepahe.com/anime/5e249027-c027-e9bc-c3de-eea9f0f64519")
# TEMPLATE = Anime("Dragon Ball Z: Saiya-jin Zetsumetsu Keikaku", "https://animepahe.com/anime/f749472f-8121-3030-0273-124b287bcf85")
# TEMPLATE = Anime("Dragon Ball Z: Atsumare! Gokuu World", "https://animepahe.com/anime/0e057dd6-7df0-a539-fd99-560ad15f8d06")
# TEMPLATE = Anime("Dragon Ball Z Special 2: Zetsubou e no Hankou!! Nokosareta Chousenshi - Gohan to Trunks", "https://animepahe.com/anime/e4e5cbff-5f33-2b5a-f260-d16aad56dc82")
# TEMPLATE = Anime("[Bardock] 1. Dragon Ball: Episode of Bardock", "https://animepahe.com/anime/ce47fd6c-c3d0-463b-e657-57ccc92915bb")
# TEMPLATE = Anime("[Bardock] 2. Dragon Ball Z Special 1: Tatta Hitori no Saishuu Kessen", "https://animepahe.com/anime/c9076696-bda0-7c3e-62d7-938314d2de9a")
# TEMPLATE = Anime("Dragon Ball Z Movie 13: Ryuuken Bakuhatsu!! Gokuu ga Yaraneba Dare ga Yaru", "https://animepahe.com/anime/c0d47c9e-eed6-ff23-809c-dbd1dcd84235")
# TEMPLATE = Anime("Dragon Ball Z Movie 12: Fukkatsu no Fusion!! Gokuu to Vegeta", "https://animepahe.com/anime/82cf4510-3cc4-6a72-bcdd-988df163d942")
# TEMPLATE = Anime("Dragon Ball Z Movie 11: Super Senshi Gekiha!! Katsu no wa Ore da", "https://animepahe.com/anime/3ec10de1-1b3e-15ad-645d-501a41528945")
# TEMPLATE = Anime("Dragon Ball Z Movie 10: Kiken na Futari! Super Senshi wa Nemurenai", "https://animepahe.com/anime/634116d2-42f2-5396-d699-3bbf46690278")
# TEMPLATE = Anime("Dragon Ball Z Movie 09: Ginga Girigiri!! Bucchigiri no Sugoi Yatsu", "https://animepahe.com/anime/2cd6e348-68d7-583c-6120-0536e3d4b935")
# TEMPLATE = Anime("Dragon Ball Z Movie 08: Moetsukiro!! Nessen, Ressen, Chougekisen", "https://animepahe.com/anime/7fe3bad5-243c-1dea-8caa-474c5c8e8041")
# TEMPLATE = Anime("Dragon Ball Z Movie 07: Kyokugen Battle!! Sandai Super Saiyajin", "https://animepahe.com/anime/f41f9306-a41d-c3b5-3686-26b316c765ad")
# TEMPLATE = Anime("Dragon Ball Z Movie 06: Gekitotsu!! 100-oku Power no Senshi-tachi", "https://animepahe.com/anime/47165437-44a9-4f7f-0625-1bbe3de35470")
# TEMPLATE = Anime("Dragon Ball Z Movie 05: Tobikkiri no Saikyou tai Saikyou", "https://animepahe.com/anime/939ad0dc-9b85-a12e-10b2-35c2253913fa")
# TEMPLATE = Anime("Dragon Ball Z Movie 04: Super Saiyajin da Son Gokuu", "https://animepahe.com/anime/f2e95914-eb12-c9e3-69bf-8b5f6ca02dbb")
# TEMPLATE = Anime("Dragon Ball Z Movie 03: Chikyuu Marugoto Choukessen", "https://animepahe.com/anime/f863790a-a1d6-376e-ac84-3c4be1c8368c")
# TEMPLATE = Anime("Dragon Ball Z Movie 02: Kono Yo de Ichiban Tsuyoi Yatsu", "https://animepahe.com/anime/e921a408-2b05-2bbf-f2f5-92006daed6a9")
# TEMPLATE = Anime("Dragon Ball Z Movie 01: Ora no Gohan wo Kaese!!", "https://animepahe.com/anime/2b04653a-7358-a876-89e5-99812d6c3350")
# TEMPLATE = Anime("Dragon Ball Specials", "https://animepahe.com/anime/119bb4eb-bcdb-f06c-8f23-628d03f5bd07")
# TEMPLATE = Anime("Dragon Ball Movie 4: Saikyou e no Michi", "https://animepahe.com/anime/079ff8fd-9f1f-3071-e77b-898fcbf4a02b")
# TEMPLATE = Anime("Dragon Ball Movie 3: Makafushigi Daibouken", "https://animepahe.com/anime/a05007f3-ee87-4b2e-d0a5-d3e9e32d3cce")
# TEMPLATE = Anime("Dragon Ball Movie 2: Majinjou no Nemurihime", "https://animepahe.com/anime/ea597e5c-25e2-db46-379b-1d50f50304a1")
# TEMPLATE = Anime("Dragon Ball Movie 1: Shen Long no Densetsu", "https://animepahe.com/anime/96b46140-977b-89ae-00ca-15caab05d89b")
# TEMPLATE = Anime("Dragon Ball Z Movie 15: Fukkatsu no \"F\"", "https://animepahe.com/anime/053643b9-dac9-1792-6a31-dc8a2d9b19ef")
# TEMPLATE = Anime("Dragon Ball Z Movie 14: Kami to Kami", "https://animepahe.com/anime/21e24f50-8c1d-df51-8192-f9e006b2f092")
# TEMPLATE = Anime("6. Dragon Ball Super Movie_ Broly", "https://animepahe.com/anime/14043b83-04d1-04dd-ac7e-bd5abf257bf6")
# TEMPLATE = Anime("5. Dragon Ball Super", "https://animepahe.com/anime/a6ee7e98-b4ac-00c4-8dac-c979f7f0b1a8")
# TEMPLATE = Anime("Dragon Ball Kai: Mirai ni Heiwa wo! Goku no Tamashii yo Eien ni", "https://animepahe.com/anime/d51b6f76-5536-26ce-4814-f545c377c18c")
# TEMPLATE = Anime("Dragon Ball Kai (2014)", "https://animepahe.com/anime/61d1413a-f03a-0782-6e9d-ac734a24f390")
# DRAGON_BALL_Z = Anime("Dragon Ball Z", "https://animepahe.com/anime/6fe1fd7f-2ee5-5542-d4cb-8383eae7e6b7")
# DRAGON_BALL = Anime("Dragon Ball", "https://animepahe.com/anime/78ba1257-76ee-83bf-bb35-40a6a16506fb")
# DRAGON_BALL_GT = Anime("Dragon Ball GT", "https://animepahe.com/anime/912bfdd0-1db1-c73a-d434-b1f47f74edbe")
# DRAGON_BALL_GT_1 = Anime("Dragon Ball GT_ Gokuu Gaiden! Yuuki no Akashi wa Suushinchuu", "https://animepahe.com/anime/d2a9b010-b5bc-7eca-6e06-5bbb5ec8b120")
# DRAGON_BALL_KAI = Anime("Dragon Ball Kai", "https://animepahe.com/anime/362a11a7-aaaf-f9e2-51f5-9cc32c19ebfd")

CURRENT_DOWNLOAD = TEMPLATE
