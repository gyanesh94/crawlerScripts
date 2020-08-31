# Basic File Location Constants
BASE_PATH = "/Users/gyanesh/Documents/Web Novels/websites"

# Constants
NOVEL_NAME = "name"
SUMMARY_URL = "summary_url"
CHAPTER_URL = "chapter_url"
CHAPTER_START = "chapter_start"
CHAPTER_END = "chapter_end"
CHAPTER_URL_IN_SEQUENTIAL = "sequential"
URL_EXCLUDE_LIST = "exclude_list"
NOVEL_INDEX = "novel_index"

NOVEL_LOCAL_FULL_PATH = "full_path"

# XPath Constants
SUMMARY_PAGE_A_LINK_XPATH = "//div[@class='panel-group']//div[@class='panel-body']//a"

# Novels Data
NOVEL_URLS = []
COMPLETED_NOVEL_URLS = []
PREVIEW_NOVEL_URLS = []
STOPPED_NOVEL_URLS = []

NOVEL_URLS.append({
    NOVEL_NAME: "A Record of a Mortal's Journey to Immortality",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/rmji",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/rmji/rmji-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 1220
})

NOVEL_URLS.append({
    NOVEL_NAME: "Against the Gods",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/against-the-gods",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/against-the-gods/atg-chapter-{}",
    CHAPTER_START: 0,
    CHAPTER_END: 1624,
    URL_EXCLUDE_LIST: (
        "https://www.wuxiaworld.com/novel/against-the-gods/atg-chapter-1044",
        "https://www.wuxiaworld.com/novel/against-the-gods/atg-chapter-1043"
    )
})

NOVEL_URLS.append({
    NOVEL_NAME: "Almighty Sword Domain",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/almighty-sword-domain",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/almighty-sword-domain/asd-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 117
})

NOVEL_URLS.append({
    NOVEL_NAME: "Archfiend",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/archfiend",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/archfiend/af-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 501,
    URL_EXCLUDE_LIST: (
        "https://www.wuxiaworld.com/novel/archfiend/af-chapter-153",
        "https://www.wuxiaworld.com/novel/archfiend/af-chapter-59",
        "https://www.wuxiaworld.com/novel/archfiend/af-chapter-288",
        "https://www.wuxiaworld.com/novel/archfiend/af-chapter-87",
        "https://www.wuxiaworld.com/novel/archfiend/af-chapter-454"
    )
})

COMPLETED_NOVEL_URLS.append({
    NOVEL_NAME: "Battle Through the Heavens",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/battle-through-the-heavens",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/battle-through-the-heavens/btth-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 1648,
})

NOVEL_URLS.append({
    NOVEL_NAME: "Beastmaster of the Ages",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/beastmaster-of-the-ages",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/beastmaster-of-the-ages/bota-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 68,
})

COMPLETED_NOVEL_URLS.append({
    NOVEL_NAME: "City of Sin",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/city-of-sin",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/city-of-sin/cos-chapter-{}",
    CHAPTER_START: 0,
    CHAPTER_END: 1420,
    URL_EXCLUDE_LIST: (
        "https://www.wuxiaworld.com/novel/city-of-sin/cos-chapter-27",
        "https://www.wuxiaworld.com/novel/city-of-sin/cos-chapter-29",
        "https://www.wuxiaworld.com/novel/city-of-sin/cos-chapter-36",
        "https://www.wuxiaworld.com/novel/city-of-sin/cos-chapter-23",
        "https://www.wuxiaworld.com/novel/city-of-sin/cos-chapter-39",
        "https://www.wuxiaworld.com/novel/city-of-sin/cos-chapter-22",
        "https://www.wuxiaworld.com/novel/city-of-sin/cos-chapter-7",
        "https://www.wuxiaworld.com/novel/city-of-sin/cos-chapter-30",
        "https://www.wuxiaworld.com/novel/city-of-sin/cos-chapter-37",
        "https://www.wuxiaworld.com/novel/city-of-sin/cos-chapter-194",
        "https://www.wuxiaworld.com/novel/city-of-sin/cos-chapter-45",
        "https://www.wuxiaworld.com/novel/city-of-sin/cos-chapter-31",
        "https://www.wuxiaworld.com/novel/city-of-sin/cos-chapter-24",
        "https://www.wuxiaworld.com/novel/city-of-sin/cos-chapter-28"
    )
})

NOVEL_URLS.append({
    NOVEL_NAME: "Demoness's Art of Vengeance",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/demoness-art-of-vengeance",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/demoness-art-of-vengeance/dav-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 25
})

COMPLETED_NOVEL_URLS.append({
    NOVEL_NAME: "Desolate Era",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/desolate-era",
    CHAPTER_URL_IN_SEQUENTIAL: False
})

COMPLETED_NOVEL_URLS.append({
    NOVEL_NAME: "Destroyer of Ice and Fire",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/destroyer-of-ice-and-fire",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/destroyer-of-ice-and-fire/dif-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 463,
    URL_EXCLUDE_LIST: (
        "https://www.wuxiaworld.com/novel/destroyer-of-ice-and-fire/dif-chapter-44",
        "https://www.wuxiaworld.com/novel/destroyer-of-ice-and-fire/dif-chapter-154",
        "https://www.wuxiaworld.com/novel/destroyer-of-ice-and-fire/dif-chapter-329",
        "https://www.wuxiaworld.com/novel/destroyer-of-ice-and-fire/dif-chapter-330",
        "https://www.wuxiaworld.com/novel/destroyer-of-ice-and-fire/dif-chapter-331"
    )
})

NOVEL_URLS.append({
    NOVEL_NAME: "Divine Throne of Primordial Blood",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/divine-throne-of-primordial-blood",
    CHAPTER_URL_IN_SEQUENTIAL: False
})

NOVEL_URLS.append({
    NOVEL_NAME: "Dragon Prince Yuan",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/dragon-prince-yuan",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/dragon-prince-yuan/yz-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 423
})

PREVIEW_NOVEL_URLS.append({
    NOVEL_NAME: "Dragon Talisman",
    SUMMARY_URL: "https://www.wuxiaworld.com/preview/dragon-talisman",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/preview/dragon-talisman/dt-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 43
})

NOVEL_URLS.append({
    NOVEL_NAME: "Dungeon Predator",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/dungeon-predator",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/dungeon-predator/dp-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 21
})

NOVEL_URLS.append({
    NOVEL_NAME: "Emperor's Domination",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/emperors-domination",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/emperors-domination/emperor-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 2689
})

NOVEL_URLS.append({
    NOVEL_NAME: "Everlasting",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/everlasting",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/everlasting/ev-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 250
})

NOVEL_URLS.append({
    NOVEL_NAME: "Everyone is Young Except for Me",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/everyone-is-young-except-for-me",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/everyone-is-young-except-for-me/eyem-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 18
})

NOVEL_URLS.append({
    NOVEL_NAME: "Fields of Gold",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/fields-of-gold",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/fields-of-gold/fog-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 469
})

COMPLETED_NOVEL_URLS.append({
    NOVEL_NAME: "Fortunately, I Met You",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/fortunately-i-met-you",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/fortunately-i-met-you/fimy-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 25
})

NOVEL_URLS.append({
    NOVEL_NAME: "Game of Divine Thrones",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/game-of-divine-thrones",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/game-of-divine-thrones/gdt-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 7
})

NOVEL_URLS.append({
    NOVEL_NAME: "Gate of Revelation",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/gate-of-revelation",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/gate-of-revelation/gor-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 753,
    URL_EXCLUDE_LIST: (
        "https://www.wuxiaworld.com/novel/gate-of-revelation/gor-chapter-352",
        "https://www.wuxiaworld.com/novel/gate-of-revelation/gor-chapter-156",
        "https://www.wuxiaworld.com/novel/gate-of-revelation/gor-chapter-608",
        "https://www.wuxiaworld.com/novel/gate-of-revelation/gor-chapter-603",
        "https://www.wuxiaworld.com/novel/gate-of-revelation/gor-chapter-325",
        "https://www.wuxiaworld.com/novel/gate-of-revelation/gor-chapter-336",
        "https://www.wuxiaworld.com/novel/gate-of-revelation/gor-chapter-607",
        "https://www.wuxiaworld.com/novel/gate-of-revelation/gor-chapter-151",
        "https://www.wuxiaworld.com/novel/gate-of-revelation/gor-chapter-268",
        "https://www.wuxiaworld.com/novel/gate-of-revelation/gor-chapter-239",
        "https://www.wuxiaworld.com/novel/gate-of-revelation/gor-chapter-143",
        "https://www.wuxiaworld.com/novel/gate-of-revelation/gor-chapter-256",
        "https://www.wuxiaworld.com/novel/gate-of-revelation/gor-chapter-192",
        "https://www.wuxiaworld.com/novel/gate-of-revelation/gor-chapter-146",
        "https://www.wuxiaworld.com/novel/gate-of-revelation/gor-chapter-353",
        "https://www.wuxiaworld.com/novel/gate-of-revelation/gor-chapter-171",
        "https://www.wuxiaworld.com/novel/gate-of-revelation/gor-chapter-270",
        "https://www.wuxiaworld.com/novel/gate-of-revelation/gor-chapter-158",
        "https://www.wuxiaworld.com/novel/gate-of-revelation/gor-chapter-155",
        "https://www.wuxiaworld.com/novel/gate-of-revelation/gor-chapter-173",
        "https://www.wuxiaworld.com/novel/gate-of-revelation/gor-chapter-241",
        "https://www.wuxiaworld.com/novel/gate-of-revelation/gor-chapter-175",
        "https://www.wuxiaworld.com/novel/gate-of-revelation/gor-chapter-612",
        "https://www.wuxiaworld.com/novel/gate-of-revelation/gor-chapter-625",
        "https://www.wuxiaworld.com/novel/gate-of-revelation/gor-chapter-170",
        "https://www.wuxiaworld.com/novel/gate-of-revelation/gor-chapter-630",
        "https://www.wuxiaworld.com/novel/gate-of-revelation/gor-chapter-272",
        "https://www.wuxiaworld.com/novel/gate-of-revelation/gor-chapter-162",
        "https://www.wuxiaworld.com/novel/gate-of-revelation/gor-chapter-152",
        "https://www.wuxiaworld.com/novel/gate-of-revelation/gor-chapter-157",
        "https://www.wuxiaworld.com/novel/gate-of-revelation/gor-chapter-321",
        "https://www.wuxiaworld.com/novel/gate-of-revelation/gor-chapter-382",
        "https://www.wuxiaworld.com/novel/gate-of-revelation/gor-chapter-144",
        "https://www.wuxiaworld.com/novel/gate-of-revelation/gor-chapter-253",
        "https://www.wuxiaworld.com/novel/gate-of-revelation/gor-chapter-164",
        "https://www.wuxiaworld.com/novel/gate-of-revelation/gor-chapter-601",
        "https://www.wuxiaworld.com/novel/gate-of-revelation/gor-chapter-223"
    )
})

NOVEL_URLS.append({
    NOVEL_NAME: "Genius Detective",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/genius-detective",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/genius-detective/gd-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 25
})

NOVEL_URLS.append({
    NOVEL_NAME: "Heaven's Devourer",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/heavens-devourer",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/heavens-devourer/hd-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 503
})

COMPLETED_NOVEL_URLS.append({
    NOVEL_NAME: "Heavenly Jewel Change",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/heavenly-jewel-change",
    CHAPTER_URL_IN_SEQUENTIAL: False
})

NOVEL_URLS.append({
    NOVEL_NAME: "I Am Overlord",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/i-am-overlord",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/i-am-overlord/iao-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 5
})

NOVEL_URLS.append({
    NOVEL_NAME: "Immortal Devil Transformation",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/immortal-devil-transformation",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/immortal-devil-transformation/idt-chapter-{}",
    CHAPTER_START: 20,
    CHAPTER_END: 56
})

COMPLETED_NOVEL_URLS.append({
    NOVEL_NAME: "Imperial God Emperor",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/imperial-god-emperor",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/imperial-god-emperor/ige-chapter-{}",
    CHAPTER_START: 0,
    CHAPTER_END: 1384,
    URL_EXCLUDE_LIST: (
        "https://www.wuxiaworld.com/novel/imperial-god-emperor/ige-chapter-1017",
        "https://www.wuxiaworld.com/novel/imperial-god-emperor/ige-chapter-1252",
        "https://www.wuxiaworld.com/novel/imperial-god-emperor/ige-chapter-1304",
        "https://www.wuxiaworld.com/novel/imperial-god-emperor/ige-chapter-131",
        "https://www.wuxiaworld.com/novel/imperial-god-emperor/ige-chapter-132",
        "https://www.wuxiaworld.com/novel/imperial-god-emperor/ige-chapter-262",
        "https://www.wuxiaworld.com/novel/imperial-god-emperor/ige-chapter-286",
        "https://www.wuxiaworld.com/novel/imperial-god-emperor/ige-chapter-288",
        "https://www.wuxiaworld.com/novel/imperial-god-emperor/ige-chapter-290",
        "https://www.wuxiaworld.com/novel/imperial-god-emperor/ige-chapter-306",
        "https://www.wuxiaworld.com/novel/imperial-god-emperor/ige-chapter-319",
        "https://www.wuxiaworld.com/novel/imperial-god-emperor/ige-chapter-340",
        "https://www.wuxiaworld.com/novel/imperial-god-emperor/ige-chapter-365",
        "https://www.wuxiaworld.com/novel/imperial-god-emperor/ige-chapter-378",
        "https://www.wuxiaworld.com/novel/imperial-god-emperor/ige-chapter-380",
        "https://www.wuxiaworld.com/novel/imperial-god-emperor/ige-chapter-381",
        "https://www.wuxiaworld.com/novel/imperial-god-emperor/ige-chapter-382",
        "https://www.wuxiaworld.com/novel/imperial-god-emperor/ige-chapter-383",
        "https://www.wuxiaworld.com/novel/imperial-god-emperor/ige-chapter-384",
        "https://www.wuxiaworld.com/novel/imperial-god-emperor/ige-chapter-385",
        "https://www.wuxiaworld.com/novel/imperial-god-emperor/ige-chapter-386",
        "https://www.wuxiaworld.com/novel/imperial-god-emperor/ige-chapter-387",
        "https://www.wuxiaworld.com/novel/imperial-god-emperor/ige-chapter-388",
        "https://www.wuxiaworld.com/novel/imperial-god-emperor/ige-chapter-389",
        "https://www.wuxiaworld.com/novel/imperial-god-emperor/ige-chapter-390",
        "https://www.wuxiaworld.com/novel/imperial-god-emperor/ige-chapter-391",
        "https://www.wuxiaworld.com/novel/imperial-god-emperor/ige-chapter-392",
        "https://www.wuxiaworld.com/novel/imperial-god-emperor/ige-chapter-393",
        "https://www.wuxiaworld.com/novel/imperial-god-emperor/ige-chapter-394",
        "https://www.wuxiaworld.com/novel/imperial-god-emperor/ige-chapter-395",
        "https://www.wuxiaworld.com/novel/imperial-god-emperor/ige-chapter-396",
        "https://www.wuxiaworld.com/novel/imperial-god-emperor/ige-chapter-397",
        "https://www.wuxiaworld.com/novel/imperial-god-emperor/ige-chapter-418",
        "https://www.wuxiaworld.com/novel/imperial-god-emperor/ige-chapter-423",
        "https://www.wuxiaworld.com/novel/imperial-god-emperor/ige-chapter-780",
        "https://www.wuxiaworld.com/novel/imperial-god-emperor/ige-chapter-963",                
    )
})

NOVEL_URLS.append({
    NOVEL_NAME: "Invincible",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/invincible",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/invincible/inv-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 1327,
    URL_EXCLUDE_LIST: (
        "https://www.wuxiaworld.com/novel/invincible/inv-chapter-477"
    )
})

NOVEL_URLS.append({
    NOVEL_NAME: "Legend of the Dragon King",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/legend-of-the-dragon-king",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/legend-of-the-dragon-king/ldk-chapter-{}",
    CHAPTER_START: 0,
    CHAPTER_END: 640,
    URL_EXCLUDE_LIST: (
        "https://www.wuxiaworld.com/novel/legend-of-the-dragon-king/ldk-chapter-374",
        "https://www.wuxiaworld.com/novel/legend-of-the-dragon-king/ldk-chapter-521"
    )
})

NOVEL_URLS.append({
    NOVEL_NAME: "Life, Once Again!",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/life-once-again",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/life-once-again/loa-chapter-{}",
    CHAPTER_START: 0,
    CHAPTER_END: 9
})

NOVEL_URLS.append({
    NOVEL_NAME: "Lord of All Realms",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/lord-of-all-realms",
    CHAPTER_URL_IN_SEQUENTIAL: False,
})

NOVEL_URLS.append({
    NOVEL_NAME: "Love Code at the End of the World",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/love-code-at-the-end-of-the-world",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/love-code-at-the-end-of-the-world/lcew-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 5
})

PREVIEW_NOVEL_URLS.append({
    NOVEL_NAME: "Magic Apprentice",
    SUMMARY_URL: "https://www.wuxiaworld.com/preview/magic-apprentice",
    CHAPTER_URL_IN_SEQUENTIAL: False
})

NOVEL_URLS.append({
    NOVEL_NAME: "Martial God Asura",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/martial-god-asura",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/martial-god-asura/mga-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 3932,
    URL_EXCLUDE_LIST: (
        "https://www.wuxiaworld.com/novel/martial-god-asura/mga-chapter-1632"
    )
})

NOVEL_URLS.append({
    NOVEL_NAME: "Monarch of Evernight",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/monarch-of-evernight",
    CHAPTER_URL_IN_SEQUENTIAL: False,
})

NOVEL_URLS.append({
    NOVEL_NAME: "Moon's Labyrinths",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/moons-labyrinths",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/moons-labyrinths/ml-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 11
})

NOVEL_URLS.append({
    NOVEL_NAME: "Necropolis Immortal",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/necropolis-immortal",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/necropolis-immortal/necro-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 34
})

NOVEL_URLS.append({
    NOVEL_NAME: "Netherworld Investigator",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/netherworld-investigator",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/netherworld-investigator/ni-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 33,
    URL_EXCLUDE_LIST: {
        'https://www.wuxiaworld.com/novel/netherworld-investigator/ni-chapter-22'
    }
})

NOVEL_URLS.append({
    NOVEL_NAME: "Nine Star Hegemon Body Art",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/nine-star-hegemon",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/nine-star-hegemon/nshba-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 1004
})

NOVEL_URLS.append({
    NOVEL_NAME: "Otherworldly Merchant",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/otherworldly-merchant",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/otherworldly-merchant/om-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 5
})

NOVEL_URLS.append({
    NOVEL_NAME: "Overgeared",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/overgeared",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/overgeared/og-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 1156
})

NOVEL_URLS.append({
    NOVEL_NAME: "Overlord of Blood and Iron",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/overlord-of-blood-and-iron",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/overlord-of-blood-and-iron/obi-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 90
})

NOVEL_URLS.append({
    NOVEL_NAME: "Perfect World",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/perfect-world",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/perfect-world/pw-chapter-{}",
    CHAPTER_START: 0,
    CHAPTER_END: 1757,
    URL_EXCLUDE_LIST: (
        "https://www.wuxiaworld.com/novel/perfect-world/pw-chapter-477",
        "https://www.wuxiaworld.com/novel/perfect-world/pw-chapter-478"
    )
})

NOVEL_URLS.append({
    NOVEL_NAME: "Physician's Odyssey",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/physicians-odyssey",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/physicians-odyssey/po-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 385
})

PREVIEW_NOVEL_URLS.append({
    NOVEL_NAME: "Phoenix's Requiem",
    SUMMARY_URL: "https://www.wuxiaworld.com/preview/phoenixs-requiem",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/preview/phoenixs-requiem/pr-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 11
})

NOVEL_URLS.append({
    NOVEL_NAME: "Poison Physician Consort",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/poison-physician-consort",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/poison-physician-consort/ppc-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 26
})

NOVEL_URLS.append({
    NOVEL_NAME: "Ranker's Return",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/rankers-return",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/rankers-return/rr-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 17
})

NOVEL_URLS.append({
    NOVEL_NAME: "Rebirth of a Fashionista- This Life Is Soo Last Season",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/rebirth-of-a-fashionista-this-live-is-so-last-season",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/rebirth-of-a-fashionista-this-live-is-so-last-season/rof-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 30
})

COMPLETED_NOVEL_URLS.append({
    NOVEL_NAME: "Rebirth of the Thief Who Roamed the World",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/rebirth-of-the-thief-who-roamed-the-world",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/rebirth-of-the-thief-who-roamed-the-world/rotwrtw-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 995
})

NOVEL_URLS.append({
    NOVEL_NAME: "Refining the Mountains and Rivers",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/refining-the-mountains-and-rivers",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/refining-the-mountains-and-rivers/rmr-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 22
})

COMPLETED_NOVEL_URLS.append({
    NOVEL_NAME: "Renegade Immortal",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/renegade-immortal",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/renegade-immortal/rge-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 2089,
    URL_EXCLUDE_LIST: (
        'https://www.wuxiaworld.com/novel/renegade-immortal/rge-chapter-1455',
        'https://www.wuxiaworld.com/novel/renegade-immortal/rge-chapter-717',
    )
})

NOVEL_URLS.append({
    NOVEL_NAME: "Rise",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/rise",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/rise/rise-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 15
})

NOVEL_URLS.append({
    NOVEL_NAME: "Sage Monarch",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/sage-monarch",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/sage-monarch/sm-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 632
})

PREVIEW_NOVEL_URLS.append({
    NOVEL_NAME: "Sovereign of the Era",
    SUMMARY_URL: "https://www.wuxiaworld.com/preview/sovereign-of-the-era",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/preview/sovereign-of-the-era/sote-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 32
})

COMPLETED_NOVEL_URLS.append({
    NOVEL_NAME: "Sovereign of the Three Realms",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/sovereign-of-the-three-realms",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/sovereign-of-the-three-realms/sotr-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 2323,
    URL_EXCLUDE_LIST: (
        "https://www.wuxiaworld.com/novel/sovereign-of-the-three-realms/sotr-chapter-878",
        "https://www.wuxiaworld.com/novel/sovereign-of-the-three-realms/sotr-chapter-835",
        "https://www.wuxiaworld.com/novel/sovereign-of-the-three-realms/sotr-chapter-877"
    )
})

COMPLETED_NOVEL_URLS.append({
    NOVEL_NAME: "Spirit Realm",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/spirit-realm",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/spirit-realm/sr-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 1832,
    URL_EXCLUDE_LIST: (
        "https://www.wuxiaworld.com/novel/spirit-realm/sr-chapter-833"
    )
})

NOVEL_URLS.append({
    NOVEL_NAME: "Spirit Vessel",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/spirit-vessel",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/spirit-vessel/sv-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 659
})

NOVEL_URLS.append({
    NOVEL_NAME: "Star Odyssey",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/star-odyssey",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/star-odyssey/so-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 80
})

COMPLETED_NOVEL_URLS.append({
    NOVEL_NAME: "Stellar Transformations",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/stellar-transformations",
    CHAPTER_URL_IN_SEQUENTIAL: False
})

NOVEL_URLS.append({
    NOVEL_NAME: "Tales of Demons & Gods",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/tales-of-demons-and-gods",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/tales-of-demons-and-gods/tdg-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 486,
    URL_EXCLUDE_LIST: (
        "https://www.wuxiaworld.com/novel/tales-of-demons-and-gods/tdg-chapter-278",
        "https://www.wuxiaworld.com/novel/tales-of-demons-and-gods/tdg-chapter-485"
    )
})

NOVEL_URLS.append({
    NOVEL_NAME: "Talisman Emperor",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/talisman-emperor",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/talisman-emperor/te-chapter-{}",
    CHAPTER_START: 61,
    CHAPTER_END: 1693
})

COMPLETED_NOVEL_URLS.append({
    NOVEL_NAME: "Terror Infinity",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/terror-infinity",
    CHAPTER_URL_IN_SEQUENTIAL: False,
})

NOVEL_URLS.append({
    NOVEL_NAME: "The Attack of the Wastrel",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/the-attack-of-the-wastrel",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/the-attack-of-the-wastrel/aotw-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 25
})

NOVEL_URLS.append({
    NOVEL_NAME: "The Charm of Soul Pets",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 1094,
    URL_EXCLUDE_LIST: (
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-523",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-119",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-492",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-526",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-494",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-566",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-197",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-631",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-201",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-238",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-955",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-1",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-264",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-493",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-683",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-559",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-783",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-291",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-811",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-802",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-383",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-855",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-1012",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-276",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-603",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-744",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-852",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-861",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-588",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-293",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-175",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-226",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-853",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-209",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-602",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-648",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-292",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-250",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-273",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-208",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-629",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-907",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-225",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-272",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-813",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-294",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-827",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-643",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-634",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-598",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-987",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-246",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-202",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-690",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-873",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-479",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-567",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-1057",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-505",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-251",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-104",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-174",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-350",
        "https://www.wuxiaworld.com/novel/the-charm-of-soul-pets/tcosp-book-2-chapter-854"
    )
})

STOPPED_NOVEL_URLS.append({
    NOVEL_NAME: "The Divine Elements",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/the-divine-elements",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/the-divine-elements/tde-chapter-{}",
    CHAPTER_START: 0,
    CHAPTER_END: 231,
    URL_EXCLUDE_LIST: (
        "https://www.wuxiaworld.com/novel/the-divine-elements/tde-chapter-115",
        "https://www.wuxiaworld.com/novel/the-divine-elements/tde-chapter-178"
    )
})

COMPLETED_NOVEL_URLS.append({
    NOVEL_NAME: "The Godsfall Chronicles",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/the-godsfall-chronicles",
    CHAPTER_URL_IN_SEQUENTIAL: False
})

NOVEL_URLS.append({
    NOVEL_NAME: "The Grandmaster Strategist",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/the-grandmaster-strategist",
    CHAPTER_URL_IN_SEQUENTIAL: False
})

NOVEL_URLS.append({
    NOVEL_NAME: "The Second Coming of Gluttony",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/the-second-coming-of-gluttony",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/the-second-coming-of-gluttony/scog-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 208
})

COMPLETED_NOVEL_URLS.append({
    NOVEL_NAME: "The Sword and The Shadow",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/the-sword-and-the-shadow",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/the-sword-and-the-shadow/ts2-chapter-{}",
    CHAPTER_START: 0,
    CHAPTER_END: 669
})

NOVEL_URLS.append({
    NOVEL_NAME: "Tomb Raider King",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/tomb-raider-king",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/tomb-raider-king/trk-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 10
})

NOVEL_URLS.append({
    NOVEL_NAME: "TranXending Vision",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/tranxending-vision",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/tranxending-vision/tv-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 728
})

NOVEL_URLS.append({
    NOVEL_NAME: "Trash of the Count's Family",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/trash-of-the-counts-family",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/trash-of-the-counts-family/tcf-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 454
})

COMPLETED_NOVEL_URLS.append({
    NOVEL_NAME: "Upgrade Specialist in Another World",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/upgrade-specialist-in-another-world",
    CHAPTER_URL_IN_SEQUENTIAL: False
})

NOVEL_URLS.append({
    NOVEL_NAME: "VRMMO: Passing of the Sword",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/vrmmo-passing-of-the-sword",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/vrmmo-passing-of-the-sword/vrps-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 15
})

NOVEL_URLS.append({
    NOVEL_NAME: "VRMMO: The Unrivaled",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/vrmmo-the-unrivaled",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/vrmmo-the-unrivaled/vrtu-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 60
})

NOVEL_URLS.append({
    NOVEL_NAME: "Yama Rising",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/yama-rising",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/yama-rising/yr-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 80
})
