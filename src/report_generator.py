
from pathlib import Path
from datetime import datetime


def generate_report(
    research_data: dict,
    output_file: str = "reports/research_report.md"
) -> str:
    """
    Generate and save a Markdown research report.
    """

    if not isinstance(research_data, dict):
        raise ValueError("Research data must be a dictionary.")

    if "question" not in research_data or "sources" not in research_data:
        raise ValueError("Research data is missing required fields.")

    report = [
        "# Research Report",
        "",
        f"**Research Question:** {research_data['question']}",
        f"**Total Sources:** {research_data.get('total_sources', 0)}",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "---",
        ""
    ]

    for index, source in enumerate(research_data["sources"], start=1):
        report.extend([
            f"## {index}. {source['title']}",
            "",
            f"**URL:** {source['url']}",
            "",
            "**Summary:**",
            "",
            source["summary"],
            "",
            "---",
            ""
        ])

    report_content = "\n".join(report)

    report_path = Path(output_file)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report_content, encoding="utf-8")

    return str(report_path)