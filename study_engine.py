"""
Study Execution Engine
Generates weekly study plans for Spring 2026 at Santa Ana College.
Aligned to Strang's Linear Algebra and Its Applications (4th Ed).

Certificate: Artificial Intelligence (SAC.CMAI.CA) — 15 units
  CMPR 114 Python Programming              (Spring 2026)
  CMPR 115 Python for Data Analytics       (Spring 2026)
  CMPR 158 Intro to Artificial Intelligence (TBD)
  CMPR 159 Intro to Machine Learning       (TBD)
  CMPR 169 SQL                             (TBD)
"""

import json
from datetime import date, timedelta

# Spring 2026 SAC semester
SEMESTER_START = date(2026, 2, 10)
SEMESTER_END = date(2026, 6, 2)

# Strang 4th Edition — verified section titles
PHASES = [
    {
        "name": "Pre-Semester",
        "weeks": (None,),  # special: before week 1
        "strang_sections": "1.1–1.3",
        "section_titles": [
            "1.1 Introduction",
            "1.2 Geometry of Linear Equations",
            "1.3 Gaussian Elimination",
        ],
        "focus": "Ax=b, Gaussian elimination, geometry",
        "ml_meaning": "representing features and solving systems",
    },
    {
        "name": "Phase 1",
        "weeks": (1, 2, 3, 4),
        "strang_sections": "1.4–1.7, 2.1–2.3",
        "section_titles": [
            "1.4 Matrix Notation and Matrix Multiplication",
            "1.5 Triangular Factors and Row Exchanges",
            "1.6 Inverses and Transposes",
            "1.7 Special Matrices and Applications",
            "2.1 Vector Spaces and Subspaces",
            "2.2 Solution of m Equations in n Unknowns",
            "2.3 Linear Independence, Basis, and Dimension",
        ],
        "focus": "matrices, inverses, vector spaces, independence",
        "ml_meaning": "vectors as data, redundancy, solvability",
    },
    {
        "name": "Phase 2",
        "weeks": (5, 6, 7, 8),
        "strang_sections": "2.4–2.6, 3.1–3.3",
        "section_titles": [
            "2.4 The Four Fundamental Subspaces",
            "2.5 Networks and Incidence Matrices",
            "2.6 Linear Transformations",
            "3.1 Perpendicular Vectors and Orthogonal Subspaces",
            "3.2 Inner Products and Projections onto Lines",
            "3.3 Least Squares Approximations",
        ],
        "focus": "subspaces, orthogonality, projections, least squares",
        "ml_meaning": "linear regression, best-fit prediction",
    },
    {
        "name": "Phase 3",
        "weeks": (9, 10, 11, 12),
        "strang_sections": "5.1–5.3",
        "section_titles": [
            "5.1 Introduction (Eigenvalues)",
            "5.2 Diagonalization of a Matrix",
            "5.3 Difference Equations and Powers A^k",
        ],
        "focus": "eigenvalues, eigenvectors, diagonalization",
        "ml_meaning": "PCA, spectral structure, dynamics",
    },
    {
        "name": "Phase 4",
        "weeks": (13, 14, 15, 16),
        "strang_sections": "6.1–6.3",
        "section_titles": [
            "6.1 Minima, Maxima, and Saddle Points",
            "6.2 Tests for Positive Definiteness",
            "6.3 The Singular Value Decomposition",
        ],
        "focus": "positive definite matrices, SVD",
        "ml_meaning": "embeddings, compression, large-scale PCA",
    },
]

MAX_WEEKLY_MATH_MINUTES = 90


def get_semester_week(today=None):
    """Return the current semester week number, or 0 for pre-semester."""
    if today is None:
        today = date.today()
    if today < SEMESTER_START:
        return 0
    delta = (today - SEMESTER_START).days
    week = delta // 7 + 1
    return min(week, 16)


def get_phase(week):
    """Return the phase dict for a given week number."""
    if week == 0:
        return PHASES[0]
    for phase in PHASES[1:]:
        if week in phase["weeks"]:
            return phase
    return PHASES[-1]


def generate_plan(today=None):
    """Generate the weekly study plan as a dict."""
    if today is None:
        today = date.today()
    week = get_semester_week(today)
    phase = get_phase(week)

    titles = phase["section_titles"]

    if week == 0:
        week_label = "Pre-Semester"
        days_until = (SEMESTER_START - today).days
        priority = (
            f"Complete Strang {phase['strang_sections']} before semester "
            f"starts in {days_until} day{'s' if days_until != 1 else ''}."
        )
        tasks = [
            f"Read: {', '.join(titles)}",
            "Solve 2–3 practice problems per section by hand",
            f"Connect to ML: {phase['ml_meaning']}",
        ]
    else:
        week_label = f"Week {week} ({phase['name']})"
        # Distribute sections across phase weeks
        phase_weeks = list(phase["weeks"])
        pos = phase_weeks.index(week)
        total = len(phase_weeks)
        # Map week position to section range
        start_idx = pos * len(titles) // total
        end_idx = (pos + 1) * len(titles) // total
        week_titles = titles[start_idx:end_idx] or [titles[min(pos, len(titles) - 1)]]

        priority = (
            f"Work through {week_titles[0].split(' ', 1)[0]} — {phase['focus']}."
        )
        tasks = [
            f"Read: {', '.join(week_titles)}",
            f"Relate to ML: {phase['ml_meaning']}",
            "Apply concepts in CMPR 114/115 Python assignments where possible",
        ]

    plan = {
        "date": today.isoformat(),
        "week": week_label,
        "primary_priority": priority,
        "secondary_tasks": tasks,
        "total_study_time_minutes": MAX_WEEKLY_MATH_MINUTES,
        "burnout_check": (
            "Safe. 90 minutes per week is sustainable."
            if week <= 8
            else "Safe if holding to 90-minute cap. Monitor energy."
        ),
    }
    return plan


def format_plan(plan):
    """Format the plan dict into the required output structure."""
    lines = []
    lines.append(f"**{plan['week']}** — {plan['date']}")
    lines.append("")
    lines.append(f"Primary Academic Priority:")
    lines.append(f"{plan['primary_priority']}")
    lines.append("")
    lines.append("Secondary Tasks:")
    for task in plan["secondary_tasks"]:
        lines.append(f"* {task}")
    lines.append("")
    lines.append("Total Study Time:")
    lines.append(f"{plan['total_study_time_minutes']} minutes")
    lines.append("")
    lines.append("Burnout Check:")
    lines.append(plan["burnout_check"])
    return "\n".join(lines)


def format_html(plan):
    """Generate a standalone HTML page for the current plan."""
    week = get_semester_week(date.fromisoformat(plan["date"]))
    total_weeks = 16
    progress_pct = 0 if week == 0 else round(week / total_weeks * 100)

    phase = get_phase(week)
    roadmap_html = ""
    for p in PHASES:
        is_current = p["name"] == phase["name"]
        cls = "current" if is_current else ""
        roadmap_html += (
            f'<div class="phase {cls}">'
            f'<strong>{p["name"]}</strong><br>'
            f'Strang {p["strang_sections"]}<br>'
            f'<span class="ml">ML: {p["ml_meaning"]}</span>'
            f'</div>\n'
        )

    tasks_html = "".join(f"<li>{t}</li>" for t in plan["secondary_tasks"])

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Spring 2026 SAC — Study Plan</title>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ font-family: -apple-system, system-ui, sans-serif; background: #0d1117;
         color: #c9d1d9; max-width: 640px; margin: 0 auto; padding: 24px 16px; }}
  h1 {{ font-size: 1.3rem; color: #58a6ff; margin-bottom: 4px; }}
  .date {{ color: #8b949e; font-size: 0.85rem; margin-bottom: 20px; }}
  .card {{ background: #161b22; border: 1px solid #30363d; border-radius: 8px;
           padding: 16px; margin-bottom: 16px; }}
  .card h2 {{ font-size: 1rem; color: #f0f6fc; margin-bottom: 8px; }}
  .priority {{ color: #58a6ff; font-size: 1.05rem; }}
  ul {{ padding-left: 20px; }}
  li {{ margin-bottom: 4px; }}
  .bar-bg {{ background: #21262d; border-radius: 6px; height: 8px; margin: 8px 0; }}
  .bar-fill {{ background: #238636; height: 8px; border-radius: 6px; }}
  .meta {{ display: flex; justify-content: space-between; font-size: 0.85rem; color: #8b949e; }}
  .roadmap {{ display: flex; flex-direction: column; gap: 8px; }}
  .phase {{ background: #21262d; border-radius: 6px; padding: 10px 12px; font-size: 0.85rem; }}
  .phase.current {{ border-left: 3px solid #58a6ff; background: #1c2333; }}
  .ml {{ color: #8b949e; font-size: 0.8rem; }}
  .burnout {{ color: #238636; font-size: 0.85rem; }}
  footer {{ margin-top: 24px; color: #484f58; font-size: 0.75rem; text-align: center; }}
</style>
</head>
<body>
<h1>{plan["week"]}</h1>
<div class="date">Generated {plan["date"]}</div>

<div class="card">
  <h2>Priority</h2>
  <p class="priority">{plan["primary_priority"]}</p>
</div>

<div class="card">
  <h2>Tasks</h2>
  <ul>{tasks_html}</ul>
</div>

<div class="card">
  <h2>Semester Progress</h2>
  <div class="bar-bg"><div class="bar-fill" style="width:{progress_pct}%"></div></div>
  <div class="meta">
    <span>Week {week} / {total_weeks}</span>
    <span>{plan["total_study_time_minutes"]} min this week</span>
  </div>
</div>

<div class="card">
  <h2>Roadmap</h2>
  <div class="roadmap">{roadmap_html}</div>
</div>

<div class="card">
  <p class="burnout">{plan["burnout_check"]}</p>
</div>

<footer>Spring 2026 SAC &middot; AI Certificate &middot; Auto-updated weekly</footer>
</body>
</html>"""


def save_plan(plan, path="plans"):
    """Save plan to a markdown file and JSON."""
    import os
    os.makedirs(path, exist_ok=True)

    formatted = format_plan(plan)
    week_slug = plan["week"].replace(" ", "_").replace("(", "").replace(")", "")
    md_path = os.path.join(path, f"{week_slug}.md")
    json_path = os.path.join(path, f"{week_slug}.json")

    with open(md_path, "w") as f:
        f.write(formatted + "\n")

    with open(json_path, "w") as f:
        json.dump(plan, f, indent=2)

    return md_path, json_path


def build_site(output_dir="site"):
    """Build the GitHub Pages site."""
    import os
    os.makedirs(output_dir, exist_ok=True)
    plan = generate_plan()
    html = format_html(plan)
    index_path = os.path.join(output_dir, "index.html")
    with open(index_path, "w") as f:
        f.write(html)
    return index_path


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "build-site":
        path = build_site()
        print(f"Site built: {path}")
    else:
        plan = generate_plan()
        print(format_plan(plan))
        md_path, json_path = save_plan(plan)
        print(f"\nSaved to: {md_path}, {json_path}")
