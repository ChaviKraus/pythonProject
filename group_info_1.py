# make content groups from back cover text (takzir)

# run the  search_prog_1.py program in idle or pycharm etc

proza = [
    [{"פרוזה": []}],
    [{"ספרים מצחיקים": ["משעשע", "מבדר", "מצחיק"]}],
    [{"מבוסס על סיפור אמיתי": ["המבוסס על חייהם", "סיפורה האמיתי", "סיפורו האמיתי", "אירועים אמיתיים"]}],
    [{"רומן היסטורי": ["הרומן ההיסטורי"]}],
    [{'להטב״ק': []}],
    [{"אימוץ": ["לאמץ תינוק", "הורים מאמצים", ]}],
    [{"רומן גרפי": []}],
    [{"קומיקס": []}],
    [{"ארכיאולוגיה": ["ארכיאולוג"]}],
    [{"התאבדות": []}],
    [{"שנות השבעים": ["סבנטיז", "שנת שבעים"]}],
    [{"רומן ריגול": ["ריגול", "מרגל", "המוסד", "CIA", "סי.איי.איי"]}],
    [{"הלם קרב": ["פוסט טראומ"]}],
    [{"יחסים מסוכנים": ["ניצול רגשי", "ניצול מיני", "אונס", "מניפולטיבי", "כופה", "תקיפה מינית"]}],
    [{"מונולוגים": ["מונולוג"]}],
    [{"נוסטלגיה": ["נוסטלגי", "געגועים לתקופ", "געגוע לימים", "געגוע לשנות"]}],
    [{"צדק חברתי": ["גלובליז", "מחא", "מהפכ"]}],
    [{"בדואים": ["בדואי", "בדווי"]}],
    [{"סיני": []}],
    [{"מלחמת לבנון השנייה": ["לבנון השני"]}],
    [{"רומן עתידני": ["עתידני"]}],
    [{"רומן פילוסופי": ["פילוסופי"]}],
    [{"סחר בבני אדם": ["עבדות", "סחר בנשים", "סחר בבני"]}],
    [{"מתחזים": ["התחז", "מתחז", "זהות בדויה", "זהות שנגנבה"]}],
    [{"מסעות במרחב וברוח": ["מסע רוחני"]}],
    [{"סוחט דמעות": ["סוחט דמעות", "סוחטת דמעות", "עד דמע"]}],
    [{"חום ושרב": ["חמסין", "שרבי", "קיץ חם"]}],
    [{"סטודנטים": ["סטודנט"]}],
    [{"דבורים": ["דבור", "כוורת"]}],
    [{"ספרים מפחידים": ["אימה", "פחד", "מפחיד", "מקפיא"]}],
    [{"אל הכוכבים": ["חלל", "כוכב"]}],
    [{"טייסים": ["טייס", "טיסה", "חיל האוויר"]}],
    [{"זהות לבנטינית": ["לבנטיני"]}],
    [{"כתבי עת": ["כתב העת", "כתב עת"]}],
    [{"הכרויות ודייטים": ["דייטינג"]}],
    [{"תודעה": []}],
    [{"גיבורים בלבן": ["רופא"]}],
    [{"הישרדות": ["הישרדות", "לשרוד"]}],
    [{"ספרות פלסטינית": []}],
    [{"בדידות": ["בודד"]}],
    [{"סוף טוב": []}],
    [{"ספרות ניסיונית": []}],
    [{"ספרים מרגיעים ומנחמים": []}],
    [{"MeToo#": []}],
    [{"סיפורים מהקליניקה": []}],
    [{"רומן בסיפורים": []}],
    [{"אחיות": ["אחות"]}],
    [{"הסדרה הקטנה": []}],
    [{"ספריה לעם": []}],
    [{"ספורטאים 🏆": ["ספורטאים"]}],
    [{"אמנים": []}],
    [{"אוטוביוגרפיה": ["אוטוביוגרפי"]}],
    [{"ממואר": []}],
    [{"טרשת נפוצה": []}],
    [{"סרטן והחלמה": []}],
    [{"ריצה": []}],

    [{"מדינות וערים": []}],
    [{"איטליה": ["סיציליה", "רומא"]}],
    [{"ניו יורק": ["מנהטן"]}],
    [{"נורווגיה": ["נורווג", "אוסלו"]}],
    [{"אירלנד": ["אירי", "אירלנד", "דבלין", "דאבלין"]}],
    [{"איסלנד": []}],
]

proza_makor = [
    [{"פרוזה מקור": []}],
    [{"קיבוץ": ["בן הקיבוץ", ]}],
]

proza_tirgum = [
    [{"פרוזה תרגום": []}],
    [{"רומן היסטורי אמריקאי": ["היסטוריה אמריקאי", "ההיסטוריה האמר", "ההיסטוריה של ארה", ]}],
    [{"סדרת חוצפנית": ["הסדרה חוצפנית"]}],
    [{"יהודים": []}],

]

action = [
    [{"מתח ופעולה": []}],
    [{"מותחן פסיכולוגי": []}],
    [{"שנות השבעים": ["סבנטיז", "שנת שבעים"]}],
    [{"סדרת הפקד מגרה": ["פקד מגרה"]}],
    [{"ספרים מפחידים": ["אימה", "פחד", "מפחיד", "מקפיא"]}],
    [{"טייסים": ["טייס", "טיסה", "חיל האוויר"]}],
    [{"סדרת מילניום": []}],
]

romantica = [
    [{"רומן רומנטי": []}],
    [{"רומנטיקת נקמה": []}],
    [{"יוונים רומנטיים": ["ליוון", "המאפיה היוונית"]}],
    [{"יחסים מסוכנים": ["ניצול רגשי", "ניצול מיני", "אונס", "מניפולטיבי", "כופה", "תקיפה מינית"]}],
    [{"רומנטיקת נקמה": ["תגמול", "לנקום", "לפרוע", "להכות בחזרה", "לגמול", "גמול", "להעניש", "עונש", "נענש", "מעניש",
                        "נמסיס", "נקם", "נקמ", "נוקם", "נוקמ", "לנקום", "נקמני", "טינה", "נוטר", ]}],
    [{"יוונים רומנטיים": ["ליוון", "מיוון", "אתונה", "סלוניקי", "כרתים", "רודוס", "קורפו", "יווני", "מיקונוס",
                          "המאפיה היוונית"]}],
    [{"יחסים מסוכנים": ["ניצול רגשי", "ניצול מיני", "התעלל", "ניצול", "ניצל", "נוצל", "השתמש", "כפה", "לכפות", "תקיפה",
                        "תקף", "תוקף", "מותקפ", "מניפול", "מתעלל", "הפחדה", "הפחיד", "פוחד", "פחד", "בעתה", "מבועת",
                        "קורבן", "נפלה", "ערמומי", "סאדיסט", "אכזר", "פסיכופת", "טורף", "טרף", "אורב", "סאדיזם",
                        "מזוכיסט", "מאזוכיזם", "אנס", "אונס", "פגיעה", "פגע" "תקיפה מינית"]}],
    [{"פנטזיה אורבנית רומנטית": ["אורבאני", "אורבני"]}],
    [{"רומנטיקה שנונה": ["מקורי", "הומוריסטי", "קומי", "מצחיק", "משעשע", "מפתיע", "לא צפוי", "קומדי", "מהנה", "צחוק",
                         "צוחק", "שנון", "שנונ", "אקסצנטרי", "מבריק", ]}],
    [{"כבאים רומנטיים": ["כבאי", "לוחם אש", "לוחמת אש", "תחנת כיבוי", "תחנת הכיבוי"]}],
    [{"סדרת קאת'רין קרופילד: ציידת הלילה": ["ציידת הלילה"]}],
    [{"גיבורים בלבן": ["רופא", "אחות", "רפואה", "להציל את חייו", "מנתח", "ניתוח", "וטרינר", "מרפאה", "חולים", "דוקטור",
                       "מחלה", "חולה"]}],
    [{"רומנטיקה גאה": ["הומו", "לסבית", "ביסקסו", "נטייתו המי", "נטייתה המ", "נטייתם המ", "אוהב גברים", "מעדיף גברים",
                       "מאוהב בבן", "קוויר", "טראנס", "טרנס"]}],
    [{"סוף טוב": ["הסוף הטוב", "עד החתונה", "מסתיים בטוב", "באושר ועושר", "מתוק", "מרגש", "מצליחה להיות", "מצליח לאהוב",
                  "מצליחים לאהוב", "מחילה", "השלמה", "תענוג", "אופטימי", "מענג", "מקסים"]}],
    [{"רומנטיקה מעוררת השראה": ["השראה", "מרגש", "בלתי נשכח", "הערצה", "מעוררת", "תקווה", "אומץ", "מסע", "חזקה",
                                "אמיצה", "לא נכנע", "נלחמת", "נלחם", ]}],
    [{"מידידים לאוהבים": ["ידיד", "חבר הכי", "שותף"]}],
    [{"קאובויים רומנטיים": ["בוקרים", "קאובוי", "על סוס"]}],
    [{"רומנטיקה בלאס וגאס": ["לאס וגאס", "לס וגאס"]}],
    [{"רופאים רומנטיים": ["רופא", "דוקטור", 'ד"ר']}],
    [{"רומנטיקה קורעת לב": ["קורע לב", "קורעת את הלב", "טראגי", "אסון", "מתמוטט", "נשבר", "מקולל", "קורבן", "הרס",
                            "מכאיב", "עצוב", "מזעזע", "טרגי"]}],
    [{"חטיפה רומנטית": ["חוטף", "כלוב", "לוכד", "חטפ", "חטף", "שפחה", "כלא", "אסירה", "אסורה", "מוכה", "נשבית", "אכזר",
                        "כלוא", "עינוי", "נעלמ"]}],
    [{"מתאבקים רומנטיים": ["מתאבק", "לוחם", "קרבות", "חטף", "הקרב", "מתאגרף", "לחימה", "תחרות", "היאבקות", "תגרה",
                           "מכות", "אגרוף", "איגרוף", "מדליה"]}],
    [{"מלאכים רומנטיים": ["מלאך", "מלאכ", "כנפיים"]}],
    [{"רומנטיקה אקזוטית": ["אקזוטי", "מדבר", "שייח", "ערבי", "שייח'", "הרמון", "סולטן"]}],
    [{"אופנוענים רומנטיים": ["אופנוע", "אגזוז", "רוכב"]}],
    [{"רומנטיקה במאפיה": ["מאפיה", "קרטל", "קארטל", "פירמידה", "מפיונ", "מאפיונ"]}],
    [{"גברי אלפא אובססיביים": ["אובסס", "קנאי", "פתייני", "אלפא", "נלאה", "לא מוותר", "מיוסר", "רודף", "רכושני",
                               "לשמצה", "קנאי", "טורף", "עוקב"]}],
    [{"סוד רומנטי": ["סוד", "חושפ", "חושף", "חשף", "מסתורי", "מוסוו", "תעלומה", "לגלות", "מגלה", "שקר", "שיקר"]}],
    [{"לטינים רומנטיים": ["לטינ", "ספרד", "מקסיק", "ארגנטינ", "פורטוגל", "דרום אמ", "צ'ילה", "קובה", "פורטו", "קולומי",
                          "קוסטה"]}],
    [{"רומנטיקה בצבא": ["צבא", "מרינס", "קצין", "חייל", "נחתים", "מפקד", "סוכן", "מבצע", "חיל האוו", "טוראי", "גנרל"]}],
    [{"רומנטיקה בהוליווד": ["הוליווד", "שחקנית", "סרטים", "כוכב"]}],
    [{"רומנטיקה בפריז": ["פריז", "פאריז", "פריס", "פאריז"]}],
    [{"מאהבת רומנטית": ["פילגש", "האישה השנייה", "מאהבת", "שוגר בייבי"]}],
    [{"הצעת נישואין רומנטית": ["מציע ני", "הצעת ני", "טבעת", "להציע ני"]}],
    [{"משולש רומן רומנטי": ["משולש", "שלושה", "שני גב", "לבחור בין"]}],
    [{"בריטים רומנטיים": ["בריט", "סקוט", "אנגלי", "לונדון"]}],
    [{"חג מולד רומנטי": ["חג מולד", "כריסטמס", "קריסטמס", "חג המולד", "אשוח", "סנטה קל"]}],
    [{"פלייבוי רומנטי": ["פלייבוי", "רודף שמלות", "קזנובה", "דון ג'ואן"]}],
    [{"צרפתים רומנטיים": ["צרפת", "פריז"]}],
    [{"איטלקים רומנטיים": ["איטלק", "נאפולי", "מילאנו", "פירנצה", "ונציה", "רומא"]}],
    [{"רוסים רומנטיים": ["רוסי", "מוסקבה", "סובייטי", "אוקראינ", "פטרסבורג", "ברית המ"]}],
    [{"הזדמנות נוספת לרומנטיקה": ["נפגשים שוב", "פעם נוספת", "להתחיל מחדש", "הזדמנות שנייה", "הפעם היא", "בפעם הקוד"]}],
    [{"ריקוד רומנטי": ["רוקד", "רקד", "בלרינה", "מחול", "חשפנ", "קברט", "כוריאוגר"]}],
    [{"פיתוי רומנטי": ["פיתוי", "מפתה", "להתפתות", "פתיי", "מושך", "מהפנט", "ממגנט"]}],
    [{"מיליונרים רומנטיים": ["מיליונר", "מיליארד", "עשיר", "אייל הון", "טייקון", "איש עסקים", "איל הון"]}],
    [{"חתונה רומנטית": ["חתונה", "מתחתנ", "מתחתן", "חופה", "הינומה", "בברית נישו", "נישאים"]}],
    [{"רומנטיקה בעבודה": ["משרד", "עובדת", "בוס", "הנהלה", "יועצת", "מזכירה", "עבודה"]}],
    [{"רומנטיקה בחופשה": ["חופש", "נופש", "מלון", "תיירת"]}],
    [{"נסיכות רומנטיות": ["נסיך", "נסיכ"]}],
    [{"רומנטיקת אהבה/שנאה": ["שונאת", "יריב", "לא סובלת"]}],
    [{"רומנטיקה מצחיקה": ["מבדר", "הומוריסטי", "קומי", "מצחיק", "משעשע", "הנאה", "כיף", "קומדי", "מהנה", "צחוק", "צוחק",
                          "שנון", "שנונ", "קורע מצח", "מבריק"]}],
    [{"רומנטיקה שמחממת את הלב": ["מחמם את הלב", "מחממת את הלב", "מרחיב לב", "שובה לב"]}],
    [{"רומנטיקה ממבט שני": ["מבט שני", "מגלה פתאום", "מתחילה להתא"]}],
    [{"רומנטיקה אסורה": ["אסורה", "אויב", "יריבות"]}],
    [{"רומנטיקה עכשווית": ["עכשווי"]}],
    [{"רומנטיקה מוזיקלית": ["מוזיק", "מוסיק", "סולן", "גיטריסט", "להקה"]}],
    [{"רומנטיקה ספורטיבית": ["ספורט", "שחקן"]}],
    [{"רומנטיקה אפלה": ["אפל", "אופל"]}],
    [{"רומנטיקה על-טבעית": ["על טבעי", "על-טבעי"]}],
    [{"רומנטיקה צעירה": ["תיכון", "טינאייג'ר", "צעיר"]}],
    [{"רומנטיקה היסטורית": ["היסטורי", "המאה ה", "בשנת"]}],
    [{"רומנטיקה בקולג'": ["קולג'", "אוניברסיט", "לימודים"]}],
    [{"גבר אלפא": ["אלפא", "שרמנטי", "כריזמטי", "יפה תואר", "אצילי", "חתיך"]}],
    [{"רומנטיקה ישראלית": ["ישראל", "תל אביב", "ירושלים", "ארץ", "במבה"]}],
    [{"פשע רומנטי": ["פשע", "פושע", "עבריין", "רוצח", "מתנקש"]}],
    [{"רומנטיקה תנכית": ["מקרא", "ספר בראשית"]}],
    [{"רומנטיקה גדולה ויפה": ["שמנה", "עודף משקל"]}],
    [{"רומנטיקה פמיניסטית": ["פמיניס", "פמניס"]}],
    [{"מורים רומנטיים": ["מורה", "גננת"]}],
    [{"רומנטיקה קלילה": ["קליל", "מלהיב", "כיף"]}],
    [{"רומנטיקה רב קולית": ["נקודות המבט", "רב קולי", "נקודות מבט"]}],
    [{"רומנטיקה פיוטית": ["פיוט", "פייוט", "נקודות מבט"]}],
    [{"בגידות רומנטיות": ["בגידה", "בוגד", "בגד"]}],
    [{"רומנטיקה נכזבת": ["שובר לב", "שברון לב", "נכזב"]}],
    [{"רומנטיקה אובססיבית": ["אובסס", "כפייתי", "סטוקר"]}],
    [{"רומנטיקה שמשאירה חיוך": ["חיוך", "הנאה", "כיף"]}],

]

erotica = [
    [{"רומן אירוטי": []}],
    [{"יחסים מסוכנים": ["ניצול רגשי", "ניצול מיני", "אונס", "מניפולטיבי", "כופה", "תקיפה מינית"]}],
    [{"יחסי שליטה": ["שולט", "שעבוד", "שפחה", "אדון", "סאדיסט", "כנועה"]}],
    [{"חטיפה אירוטית": ["חטיפה", "נחטפת", "חוטף", "נלקחת בשבי"]}],
    [{"טאבו אירוטי": ["טאבו", "סטייה", "סטיות", "סוטה"]}],
    [{"אירוטיקה ישראלית": []}],
    [{"רומנטיקה היסטורית": ["היסטורי", "המאה ה", "בשנת"]}],
    [{"רומנטיקה בלאס וגאס": ["לאס וגאס", "לס וגאס"]}],
    [{"אירוטיקה עכשווית": ["עכשווי"]}],
    [{"BDSM": ["BDSM", "סאדיז", "סאדיס", "סאדו"]}],
    [{"מותחן פשע אירוטי": ["פשע", "פושע", "עבריין", "מאפיה", "קרטל", "כנופייה"]}],
    [{"אירוטיקה אפלה": ["אפל", "אופל"]}],
    [{"מותחן אירוטי": ["מתח", "מותח"]}],

]

eyuin = [
    [{"עיון": []}],
    [{"אמנות": ["האמנות החזותית", ]}],
    [{"פשיזם": ["פשיזם", "פאשיזם"]}],
    [{"הלם קרב": ["פוסט טראומ"]}],
    [{"מונולוגים": ["מונולוג"]}],
    [{"נוסטלגיה": ["נוסטלגי", "געגועים לתקופ", "געגוע לימים", "געגוע לשנות"]}],
    [{"צדק חברתי": ["צדק", "גלובליז", "מחא", "מהפכ"]}],
    [{"בדואים": ["בדואי", "בדווי"]}],
    [{"זכויות אדם": ["זכויות"]}],
    [{"סחר בבני אדם": ["עבדות", "סחר בנשים", "סחר בבני"]}],
    [{"האנושות, לאן?": ["האנושות", "עתיד"]}],
    [{"אל הכוכבים": ["חלל", "כוכב"]}],
    [{"זהות לבנטינית": ["לבנטיני"]}],
    [{"תודעה": []}],
    [{"MeToo#": []}],
    [{"אקדמיה": []}],
    [{'בג"ץ': ["המשפט העליון"]}],
    [{"סדרת אפקים": ["אפקים"]}],
    [{"סדרת מלחינים, חייהם ויצירתם": []}],
    [{"ספורטאים 🏆": ["ספורטאים"]}],
    [{"אמנים": []}],
    [{"אוטוביוגרפיה": ["אוטוביוגרפי"]}],
    [{"זיכרונות": []}],
    [{"טבעונות": []}],
    [{"שיקום": []}],
    [{"גוף האדם": []}],
    [{"ריצה": []}],
]

fantasy = [
    [{'מד״ב ופנטזיה': []}],
    [{"מדע בדיוני": []}],
    [{"פנטזיה": ["מסע פנטסטי", ]}],
    [{"פנטזיה קומית": ["מצחיק", "צחוק", "קומי", "קומדיה", "משעשע"]}],
    [{"פנטזיה אפית": ["שר הטבעות", "משחקי הכס"]}],
    [{"רומן עתידני": ["עתידני"]}],
    [{"פנטזיה יהודית": ["יהודי", "יהדות"]}],
    [{"פנטזיה אורבנית רומנטית": ["אורבאני", "אורבני"]}],
    [{"אל הכוכבים": ["חלל", "כוכב"]}],
    [{"פנטזיה ישראלית": []}],
    [{"זומבים": []}],
    [{"קורות קצעולם": ["קצעולם"]}],
    [{"סדרת מחזור שער המוות": ["שער המוות"]}],
]

children_and_teenagers = [
    [{"ילדים ונוער": []}],
    [{"יום הולדת לילדים": ["יום הולדת", "יומולדת"]}],
    [{"קבלת השונה": []}],
    [{"קומיקס מנוקד": []}],
    [{"ציונות לילדים": []}],
    [{"נוער בשואה": []}],
    [{"דמיון מודרך לילדים": []}],
    [{"קלאסיקות ישראליות לפעוטות": []}],
    [{"סדרת גורלו של אפולו": []}],
    [{"סדרת מגנס צ'ייס והאלים של אוסגרד": []}],
    [{"סדרת משפחת קיין והאלים המצריים": []}],
    [{"סדרת גיבורי האולימפוס": []}],
    [{"סדרת פרסי ג'קסון והאולימפיים": []}],
    [{"♥ סבא וסבתא": ["סבא", "נכדתו"]}],
    [{"ספרים מנוקדים לילדים": []}],
    [{"ספרי ילדים בפורמט PDF": []}],
    [{"פעילויות לילדים": []}],
    [{"סדרת סיפורי ממלכת נרניה": []}],
    [{"ילדים ומאכלים": []}],
    [{"זומבים": []}],
    [{"סדרת ספרי אסטריקס": []}],
    [{"מיינקראפט MINECRAFT": ["מיינקראפט", "minecraft"]}],
    [{"בריאות לילדים": ["בריא", "חולה"]}],
    [{"קורות קצעולם": ["קצעולם"]}],
]

babies = [
    [{"פעוטות": []}],
    [{"סבא וסבתא": ["סבא", "נכדתו"]}],
    [{"קלאסיקות ישראליות לפעוטות": []}],
]

kinder = [
    [{"ילדי גן": []}],
    [{"סבא וסבתא": ["סבא", "נכדתו", "סבַּאָ", "סָבְתָא"]}],
    [{"פחדי ילדים": ["פּחְדָיִם", "חַרֲדָוֹת"]}],
    [{"בעלי חיים לילדים": ["חַתֲוּליִם", "חָתוּל" "קיפוד", "שועלה", "תיש" "קרנף", "זיקית", "קוֹף", "נָמֵר" "פיל",
                           "דָּג", "כלבלב", "כֶּלֶב", "כלבה", "צָב", "אַרְנָב", "דְּבוֹרָה", "תּוֹלַעַת", "חַיּוֹת",
                           "פִּינְגְוִין", "אריה", "ג׳ירפה", "ג׳ירף"]}],
    [{"יום הולדת לילדים": ["יום הולדת", "יומולדת"]}],
]

start_reading = [
    [{"ראשית קריאה": []}],
    [{"סבא וסבתא": ["סבא", "נכדתו"]}],
    [{"שירים לילדים": []}],
    [{"דילמות של ילדים": ["שיימינג"]}],
    [{"קומיקס מנוקד": []}],
]

young_teenagers = [
    [{"נוער צעיר": []}],
    [{"דילמות של ילדים": ["שיימינג"]}],
    [{"קומיקס מנוקד": []}],
]

old_teenagers = [
    [{"נוער בוגר": []}],
    [{"תיכון": []}],
]

holocaust = [
    [{"שואה": []}],
    [{"הצלה בשואה": ["הצלת יהודים"]}],
]

judaism = [
    [{"יהדות": []}],
    [{"תלמוד": ['חז״ל']}],
    [{'ל"ג בעומר': []}],
]

advice = [
    [{"מדריכים ועצות": []}],
    [{"עזרה עצמית": []}],
    [{"התפתחות אישית": []}],
    [{"הכרויות ודייטים": ["דייטינג"]}],
    [{"דיבור בפני קהל": []}],
    [{"סידור הבית": []}],
]

business = [
    [{"עסקים וניהול": []}],
    [{"אסטרטגיה עסקית": []}],
    [{"הכנה לראיונות עבודה": []}],
    [{"תכנון עסקי בתנאי אי-ודאות": []}],
    [{"דיבור בפני קהל": []}],
]

history_and_politics = [
    [{"היסטוריה ופוליטיקה": []}],
    [{"פוליטיקה": ["הפוליטיקה הישראלית"]}],
    [{"פשיזם": ["פשיזם", "פאשיזם"]}],
    [{"נוסטלגיה": ["נוסטלגי", "געגועים לתקופ", "געגוע לימים", "געגוע לשנות"]}],
    [{"צדק חברתי": ["צדק", "גלובליז", "מחא", "מהפכ"]}],
    [{"בדואים": ["בדואי", "בדווי"]}],
    [{"סיני": []}],
    [{"זכויות אדם": ["זכויות"]}],
    [{"מלחמת לבנון השנייה": ["לבנון השני"]}],
    [{"סחר בבני אדם": ["עבדות", "סחר בנשים", "סחר בבני"]}],
    [{"האנושות, לאן?": ["האנושות", "עתיד"]}],
    [{"זהות לבנטינית": ["לבנטיני"]}],
    [{"חללי מערכות ישראל": []}],
    [{"ספרות צבאית": ["צבאית"]}],
    [{"מרגלים": ["ריגול","מרגל", "סוכן" "המוסד"]}],
    [{"מסתערבים": []}],
    [{"דיקטטורים": ["דיקטטור", "שליט", "מלך"]}],
    [{"אקדמיה": []}],
    [{'בג"ץ': ["המשפט העליון"]}],
    [{"סדרת אפקים": ["אפקים"]}],
    [{"ראשי ממשלה": []}],
    [{"לוחמים": []}],
    [{"פוליטיקאים ומנהיגים": ["פוליטיקאי", "מנהיג", "נשיא", "ראש ממשלה"]}],
    [{"היסטוריה קולינרית": []}],
    [{"רנסנס והעת החדשה": ["רנסאנס", "רנסנס", "העת החדשה", " המאה ה-16", " המאה ה-17", "המאה ה-15"]}],
    [{"נאצים ועוזריהם": ["נאצי", "הרייך השלישי", "היטלר"]}],
    [{"אנטישמיות": ["אנטישמ", "שנאת יהודים", "אפליית יהו"]}],
    [{"היסטוריה ישראלית": ["היסטוריה של ישרא", "היסטוריה של מדינת יש", "היסטוריה של ארץ יש", "תולדות מדינת ישראל"]}],
    [{"נאציזם": []}],
    [{"העלייה השנייה": ["עליה שנ", "עלייה שנ", "העליה השנ", "העליה הש", "ביל"ו"]}],
    [{"העלייה הראשונה": ["עליה ראש", "עלייה ראש", "העליה הראש", "אעלה בתמר", "מושבות הברון"]}],
    [{"היסטוריה של העת העתיקה וימי הביניים": ["העת העתיק", "ימי הבינ", "תקופת הב", "אעלה בתמר", "התקופה הקלאס"]}],
    [{"מהפכות": ["מהפכת", "מהפיכת", "הפיכת", "מהפכה", "מהפכני"]}],
    [{"עידן הנאורות": ["תנועת ההשכלה", "נאורות", "המהפכה הצר", "תנועת הרומנטיקה"]}],
    [{"תהליך השלום": ["הסכם אוסלו"]}],
    [{"צבא וביטחון": ["צבא", "ביטחונ", "בטחונ", "בטחון ה", "ביטחון ה"]}],
    [{"ההתנתקות": ["גוש קטיף"]}],
    [{"מלחמת העצמאות": ["מלחמת השח", "מלחמת 48", "נאכבה", "מלחמת הקוממ"]}],
    [{"מלחמת ששת הימים": ["מלחמת ששת", "מלחמת 67"]}],
    [{"פלסטינים": ["פלשתינ", "רצועת עזה", "הגדה המז", "פלסטינ"]}],
    [{"ציונות": ["ציוני"]}],
    [{"היסטוריה יהודית": ["היסטוריה של יהו", "תולדות יהו", "תולדות היהו", "היסטוריה של היהוד"]}],
    [{"פוליטיקה": ["פוליטי"]}],               
    [{"היסטוריה": ["תולדות"]}],   
    [{"מלחמה בטרור": ["טרור"]}],
    [{"איראן": ["איראנ", "אירן", "אירנ", "פרסי", "בגדד"]}],
    [{"מודיעין": ["מודיעינ", "8200"]}],
    [{"משני עולם": ["שינה את העול", "שינתה את העול"]}],
    [{"חברה ודמוקרטיה": ["דמוקרט", "מחאה", "סוציולוג", "אנתרופולוג", "חברתי"]}],
    [{"שחיתות": ["מושחת"]}],
    [{"ישראליוּת": ["ישראלי"]}],
    [{"המלחמה הקרה": ["מסך הברזל"]}],
    [{"מלחמת העולם הראשונה": []}],
    [{"מלחמת העולם השנייה": ["מלחמת העולם הש"]}],                    
    [{"המזרח התיכון": ["מזרח תיכונ", "מזרח תיכון"]}],
    [{"מלחמת יום כיפור": ["מלחמת יום-", "מלחמת יום", "1973"]}],
    [{"מלחמות ישראל": ["מלחמת יום",  "צוק איתן", "חומת מגן", "מלחמת הש", "מלחמת המ",  "מלחמת ששת", "מלחמת ל", "מבצע סי", "מבצע של", "מבצע סי", "1973", "1967", "1948"}],                    
    [{"קולוניאליזם": ["קולוניאל", "איפריאל",]}],
    [{"הסכסוך הערבי ישראלי": ["הסכסוך הע", "הסכסוך הי",]}],
    [{"חושפי מחדלים": ["מחדל"}],
    [{"אנוסים": ["גירוש ספרד", "אנוסי, "אינקוויזי", "נוצרים חדשים", "יהדות ספ", "יהדות פורט"]}],
    [{"מחתרות": ["אצ"ל", "לח"י", "ניל"י", "תנועת המרי", "ההגנה"]}],
    [{"צה"ל": ["צבא ההגנה"]}],
    [{"מלחמת לבנון": ["שלום הגליל", "של"ג"]}],
                      
                        




]

biography = [
    [{"ביוגרפיה": []}],
    [{"ביוגרפיות": []}],
    [{"אוטוביוגרפיה": ["אוטוביוגרפי"]}],
    [{"פשיזם": ["פשיזם", "פאשיזם"]}],
    [{"הלם קרב": ["פוסט טראומ"]}],
    [{"מונולוגים": ["מונולוג"]}],
    [{"נוסטלגיה": ["נוסטלגי", "געגועים לתקופ", "געגוע לימים", "געגוע לשנות"]}],
    [{"סחר בבני אדם": ["עבדות", "סחר בנשים", "סחר בבני"]}],
    [{"מסעות במרחב וברוח": ["מסע רוחני"]}],
    [{"טייסים": ["טייס", "טיסה", "חיל האוויר"]}],
    [{"חללי מערכות ישראל": []}],
    [{"הישרדות": ["הישרדות", "לשרוד"]}],
    [{"מרגלים": []}],
    [{"מסתערבים": []}],
    [{"דיקטטורים": []}],
    [{"סדרת מלחינים, חייהם ויצירתם": []}],
    [{"ספורטאים 🏆": ["ספורטאים"]}],
    [{"אמנים": []}],
    [{"ממואר": []}],
    [{"זיכרונות": []}],
    [{"יהודים": []}],
    [{"ראשי ממשלה": []}],
    [{"לוחמים": []}],
    [{"פוליטיקאים ומנהיגים": []}],
    [{"טרשת נפוצה": []}],
    [{"סרטן והחלמה": []}],
    [{"מדענים": []}],
    [{"גאונים": []}],
    [{"זיכרונות מייסדים": []}],
    [{"מסעדנות": []}],
]

health = [
    [{"בריאות": []}],
    [{"מדע ורפואה": ["מדע", "רפוא", "ביולוג "]}],
    [{"סוכרת": ["סכרת", "סוכר"]}],
    [{"כאב": ["כואב"]}],
    [{"ALS": ["ניוון"]}],
    [{"ריצה": ["לרוץ"]}],
    [{"שינה": ["לישון"]}],
    [{"פסיכיאטריה": ["פסיכיאטר]}],
    [{"רפואה מונעת": []}],
    [{"גוף האדם": []}],
    [{"שיקום": []}],
    [{"סרטן והחלמה": ["סרטן"]}],
    [{"טבעונות": ["טבעונ]}],
    [{"ירידה במשקל": ["דיאטה"]}],
    [{"רפואה משלימה": ["דיקור", "עיסוי", "טווינ", "שיאצו" "נטורופ", "אוסטיאו", "הומיאופ", "רפלקסו", "כירופרק", "שיטת", "משלימה", "אלטרנטיבי", "אוקופ]}],
    [{"דיאטה": ["דיאט"]}],
    [{"חיים בריאים": []}],
    [{"תזונה": []}],
    [{"טרשת נפוצה": []}],
]

psychology = [
    [{"פסיכולוגיה": []}],
    [{"פסיכואנליזה": []}],
    [{"פסיכותרפיה": ["טיפול נפשי", "הטיפול הנפשי"]}],
    [{"הלם קרב": ["פוסט טראומ"]}],
    [{"מונולוגים": ["מונולוג"]}],
    [{"כאב": []}],
    [{"סיפורים מהקליניקה": []}],
    [{"לאנשים רגישים מאוד HSP": []}],
    [{"שיקום": []}],
    [{"שינה": []}],
    [{"פסיכיאטריה": []}],
    [{"כאב": []}],
]

parenting = [
    [{"הורות וזוגיות": []}],
    [{"מיניות": ["סקס", "מיני"]}],
    [{"הכרויות ודייטים": ["דייטים", "שידוכ", "שידוך", "רווקות", "דייטינג"]}],
    [{"יחסים פתוחים": ["מונוגמ", "פוליאמ", "לפתוח את הזוג", "זוגיות מאפשר", "זוגיות פתוחה", "נישואים פתוחים"]}],
    [{"הורות יחידנית": ["יחידני", "חד הורי", "חד-הורי", "תרומת זר", "אם חד"]}],
    [{"אבהות": ["להיות אבא"]}],
    [{"תזונת תינוקות": ["מזון לתינוק"]}],
    [{"הריון ופוריות": ["הריון",  "היריון", "הריונ", "היריונ", "פוריות"]}],
    [{"גירושים": ["להתגרש", "גרושים", "גרושין", "גרושי", "גירושין"]}],
    [{"זוגיות": ["זוגי", "יחסים]}],
    [{"הורות": ["הורי", "אבהות", "אימהות", "אמהות", "גידול ילד", "הורה]}],

    
    
]

philosophy = [
    [{"הגות ופילוסופיה": []}],
    [{"פילוסופיה": ["פילוסופים"]}],
    [{"פילוסופיה עתיקה": ["פילוסופיה יוונית"]}],
    [{"אקזיסטנציאליזם": ["אקזיסטנציאל"]}],
    [{"צדק חברתי": ["צדק", "גלובליז", "מחא", "מהפכ"]}],
]

spirituality = [
    [{"רוחניות": []}],
    [{"עידן חדש": ["הניו אייג'"]}],
    [{"מסעות במרחב וברוח": ["מסע לגילוי", "מסע רוחני"]}],
    [{"התפתחות אישית": []}],
    [{"מודעות": []}],
    [{"יוגה": ["יוגי", "יוגת"]}],
    [{"קבלה עצמית": []}],
    [{"תודעה": []}],
    [{"תיקשור": ["מדיום", "תקשור"]}],
    [{"ליווי רוחני": []}],
    [{"השראה": []}],
    [{"חלומות": []}],
    [{"מיינדפולנס": ["קשיבות"]}],
    [{"סגולות, לחשים וקמעות": ["קמע", "סגולות", "ברכות", "טארוט", "סגולה"]}],
    [{"מיסטיקה": ["נומרולוגי", "אסטרולוגי", "טארוט", "מיסטי"]}],
    [{"מדיטציה": ["מדיט"]}],
    [{"אסטרולוגיה": ["אסטרולוג", "הורוסקופ", "טארוט", "מיסטי"]}],
    [{"בודהיזם": ["בודהיס", "בודהה", "דהרמה", "נזיר ז"]}],
    [{"רפואה משלימה": ["דיקור", "עיסוי", "טווינ", "שיאצו" "נטורופ", "אוסטיאו", "הומיאופ", "רפלקסו", "כירופרק", "שיטת", "משלימה", "אלטרנטיבי", "אוקופ]}],
]

traveling = [
    [{"טיולים ופנאי": []}],
    [{"טיולים בארץ": []}],
    [{"סידור הבית": []}],
    [{"מסעדנות": []}],
    [{"אירוח": []}],
    [{"ריצה": []}],
]

cooking = [
    [{"בישול": []}],
    [{"מתכונים וסיפורים": []}],
    [{"יין וקוקטיילים": ["יין", "אלכוהול", "קוקטייל"]}],
    [{"שוקולד": []}],
    [{"שפים אהובים": ["השף האהוב", "שף מפורס", "שף מוכר", "השפים"]}],
    [{"פשטידות": ["פשטידה]}],
    [{"דגים": []}],
    [{"בישול בקלות": ["בישול קל", "לא מסובך", "לבשל בקלות"]}],
    [{"בשר": []}],
    [{"אירוח": ["לארח"]}],
    [{"אוכל ים תיכוני": ["תיכוני"]}],
    [{"אוכל בריא": ["בריא"]}],
    [{"כשר לפסח": []}],
    [{"בישול לפי עדות": ["מרוקאי", "טריפולי", "עיראק", "עירק", "תימנ", "תימן", "טורק", "העדה", "עדות]}],
    [{"בישול לילדים": ["ילדים"]}],
    [{"היסטוריה קולינרית": ["גסטרו", "קולינ]}],
    [{"קינוחים": ["מנות אחרו", "קינוח", "עוג"]}],
    [{"אפייה": ["לחמ", "לחמי", "עוג", "מאפה", "מאפי"]}],
    [{"בישול": ["לבשל"]}],
    [{"מסעדנות": ["מסעד]}],
    [{"טבעונות": ["טבעונ"]}],
]

poem = [
    [{"שירה": []}],
    [{"שירה עברית": []}],
    [{"ערס פואטיקה": []}],
    [{"שירה מתורגמת": ["תרגום", "תרגמ", "תורגמ", "תירגם"]}],
    [{"שירה עברית": ["ישראלי", "שירה עברית"]}],
    [{"כתבי עת": ["כתב העת", "כתב עת"]}],
    [{"שירה הומוריסטית": []}],
]

all_groups = [proza, proza_makor, proza_tirgum, action, romantica, erotica,
              eyuin, fantasy, children_and_teenagers, babies, kinder, start_reading, young_teenagers, old_teenagers,
              holocaust, judaism, advice, business, history_and_politics, biography, health,
              psychology, parenting, philosophy, spirituality, traveling, cooking, poem]
all_groups_str = ["פרוזה", "פרוזה מקור", "פרוזה תרגום", "מתח ופעולה", "רומן רומנטי", "רומן אירוטי",
                  "עיון", 'מד״ב ופנטזיה', "ילדים ונוער", "פעוטות", "ילדי גן", "ראשית קריאה", "נוער צעיר", "נוער בוגר",
                  "שואה", "יהדות", "מדריכים ועצות", "עסקים וניהול", "היסטוריה ופוליטיקה", "ביוגרפיה", "בריאות",
                  "פסיכולוגיה", "הורות וזוגיות", "הגות ופילוסופיה", "רוחניות", "טיולים ופנאי", "בישול", "שירה"]
