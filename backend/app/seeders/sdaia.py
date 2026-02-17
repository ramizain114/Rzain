"""SDAIA AI Ethics Guidelines seeder.

Based on Saudi Data & AI Authority's guidelines for ethical and responsible AI.
"""

STANDARD_META = {
    "code": "SDAIA",
    "name_en": "AI Ethics Guidelines",
    "name_ar": "مبادئ أخلاقيات الذكاء الاصطناعي",
    "description_en": "Saudi Data & AI Authority's principles and guidelines for ethical artificial intelligence",
    "description_ar": "مبادئ وإرشادات هيئة البيانات والذكاء الاصطناعي للذكاء الاصطناعي الأخلاقي",
    "version": "1.0",
    "category": "ai_ethics",
}

CONTROLS = [
    # AI Governance
    {
        "control_id": "SDAIA-1-1",
        "domain_en": "AI Governance",
        "domain_ar": "حوكمة الذكاء الاصطناعي",
        "title_en": "AI Ethics Framework",
        "title_ar": "إطار أخلاقيات الذكاء الاصطناعي",
        "description_en": "The organization shall establish an AI ethics framework defining principles, policies, and oversight mechanisms.",
        "description_ar": "يجب على الجهة إنشاء إطار أخلاقيات الذكاء الاصطناعي يحدد المبادئ والسياسات وآليات الإشراف.",
        "priority": "CRITICAL",
    },
    {
        "control_id": "SDAIA-1-2",
        "domain_en": "AI Governance",
        "domain_ar": "حوكمة الذكاء الاصطناعي",
        "title_en": "AI Impact Assessment",
        "title_ar": "تقييم تأثير الذكاء الاصطناعي",
        "description_en": "The organization shall conduct impact assessments before deploying AI systems in production.",
        "description_ar": "يجب على الجهة إجراء تقييمات التأثير قبل نشر أنظمة الذكاء الاصطناعي في الإنتاج.",
        "priority": "HIGH",
    },
    
    # Fairness and Non-Discrimination
    {
        "control_id": "SDAIA-2-1",
        "domain_en": "Fairness",
        "domain_ar": "العدالة",
        "title_en": "Bias Detection and Mitigation",
        "title_ar": "الكشف عن التحيز والحد منه",
        "description_en": "The organization shall implement mechanisms to detect and mitigate bias in AI systems.",
        "description_ar": "يجب على الجهة تطبيق آليات للكشف عن التحيز والحد منه في أنظمة الذكاء الاصطناعي.",
        "priority": "CRITICAL",
    },
    {
        "control_id": "SDAIA-2-2",
        "domain_en": "Fairness",
        "domain_ar": "العدالة",
        "title_en": "Fairness Testing",
        "title_ar": "اختبار العدالة",
        "description_en": "The organization shall regularly test AI systems for fairness across different demographic groups.",
        "description_ar": "يجب على الجهة اختبار أنظمة الذكاء الاصطناعي بانتظام للعدالة عبر مختلف المجموعات الديموغرافية.",
        "priority": "HIGH",
    },
    
    # Transparency and Explainability
    {
        "control_id": "SDAIA-3-1",
        "domain_en": "Transparency",
        "domain_ar": "الشفافية",
        "title_en": "AI System Documentation",
        "title_ar": "توثيق نظام الذكاء الاصطناعي",
        "description_en": "The organization shall document AI system capabilities, limitations, and decision-making processes.",
        "description_ar": "يجب على الجهة توثيق قدرات ومحددات وعمليات صنع القرار لنظام الذكاء الاصطناعي.",
        "priority": "HIGH",
    },
    {
        "control_id": "SDAIA-3-2",
        "domain_en": "Transparency",
        "domain_ar": "الشفافية",
        "title_en": "Explainable AI",
        "title_ar": "الذكاء الاصطناعي القابل للتفسير",
        "description_en": "The organization shall implement explainability mechanisms for AI decisions affecting individuals.",
        "description_ar": "يجب على الجهة تطبيق آليات التفسير لقرارات الذكاء الاصطناعي التي تؤثر على الأفراد.",
        "priority": "CRITICAL",
    },
    
    # Privacy and Data Protection
    {
        "control_id": "SDAIA-4-1",
        "domain_en": "Privacy",
        "domain_ar": "الخصوصية",
        "title_en": "Privacy by Design",
        "title_ar": "الخصوصية حسب التصميم",
        "description_en": "The organization shall integrate privacy protections into AI system design from the outset.",
        "description_ar": "يجب على الجهة دمج حماية الخصوصية في تصميم نظام الذكاء الاصطناعي منذ البداية.",
        "priority": "CRITICAL",
    },
    {
        "control_id": "SDAIA-4-2",
        "domain_en": "Privacy",
        "domain_ar": "الخصوصية",
        "title_en": "Data Minimization",
        "title_ar": "تقليل البيانات",
        "description_en": "The organization shall collect and process only the minimum data necessary for AI system functionality.",
        "description_ar": "يجب على الجهة جمع ومعالجة الحد الأدنى من البيانات اللازمة لوظيفة نظام الذكاء الاصطناعي فقط.",
        "priority": "HIGH",
    },
    
    # Safety and Security
    {
        "control_id": "SDAIA-5-1",
        "domain_en": "Safety",
        "domain_ar": "السلامة",
        "title_en": "AI Safety Testing",
        "title_ar": "اختبار سلامة الذكاء الاصطناعي",
        "description_en": "The organization shall conduct comprehensive safety testing before deploying AI systems.",
        "description_ar": "يجب على الجهة إجراء اختبار سلامة شامل قبل نشر أنظمة الذكاء الاصطناعي.",
        "priority": "CRITICAL",
    },
    {
        "control_id": "SDAIA-5-2",
        "domain_en": "Safety",
        "domain_ar": "السلامة",
        "title_en": "Fail-Safe Mechanisms",
        "title_ar": "آليات الأمان من الفشل",
        "description_en": "The organization shall implement fail-safe mechanisms to prevent AI system failures from causing harm.",
        "description_ar": "يجب على الجهة تطبيق آليات الأمان من الفشل لمنع فشل نظام الذكاء الاصطناعي من التسبب في ضرر.",
        "priority": "HIGH",
    },
    
    # Accountability
    {
        "control_id": "SDAIA-6-1",
        "domain_en": "Accountability",
        "domain_ar": "المساءلة",
        "title_en": "Human Oversight",
        "title_ar": "الإشراف البشري",
        "description_en": "The organization shall maintain appropriate human oversight of AI system decisions.",
        "description_ar": "يجب على الجهة الحفاظ على الإشراف البشري المناسب على قرارات نظام الذكاء الاصطناعي.",
        "priority": "CRITICAL",
    },
    {
        "control_id": "SDAIA-6-2",
        "domain_en": "Accountability",
        "domain_ar": "المساءلة",
        "title_en": "Audit Trail",
        "title_ar": "مسار التدقيق",
        "description_en": "The organization shall maintain comprehensive audit trails of AI system decisions and actions.",
        "description_ar": "يجب على الجهة الحفاظ على مسارات تدقيق شاملة لقرارات وإجراءات نظام الذكاء الاصطناعي.",
        "priority": "HIGH",
    },
]
