def get_prompt(lang: str, content_summary: str) -> str:
    if lang == "en":
        return f"Based on the following project files, generate a professional README.md:\n\n{content_summary}"
    elif lang == "ko":
        return f"다음 프로젝트 파일들을 기반으로 전문적인 README.md 파일을 생성해줘:\n\n{content_summary}"
    else:
        raise ValueError(f"Unsupported language: {lang}")