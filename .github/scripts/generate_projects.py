#!/usr/bin/env python3

import base64
import html
import json
import mimetypes
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

DARK = {
    "background": "#222831",
    "surface": "#393E46",
    "surface_2": "#30353D",
    "accent": "#948979",
    "highlight": "#DFD0B8",
    "text": "#DFD0B8",
    "muted": "#948979",
    "border": "#948979",
    "border_soft": "#525862",
}

LIGHT = {
    "background": "#DFD0B8",
    "surface": "#F5F1EA",
    "surface_2": "#FFFFFF",
    "accent": "#948979",
    "highlight": "#393E46",
    "text": "#222831",
    "muted": "#393E46",
    "border": "#948979",
    "border_soft": "#C8BFAF",
}


def escape(value):
    return html.escape(str(value or ""))


def read_projects(path):
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, list):
        raise ValueError("merged.json must contain an array.")

    return data


def image_to_data_uri(path):
    if not path.exists():
        return None

    mime, _ = mimetypes.guess_type(path.name)

    if not mime:
        mime = "image/png"

    data = path.read_bytes()

    encoded = base64.b64encode(data).decode("ascii")

    return f"data:{mime};base64,{encoded}"


def get_logo(project):
    logo = project.get("logo")

    if not logo:
        return None

    logo_path = ROOT / "logos" / logo

    return image_to_data_uri(logo_path)


def project_description(project):
    live = project.get("description_live")

    if live:
        return live

    return project.get(
        "description",
        "No description available.",
    )


def truncate(text, length=76):
    text = str(text or "")

    if len(text) <= length:
        return text

    return text[: length - 3].rstrip() + "..."


def create_svg(projects, colors, title):
    width = 1200

    card_width = 365
    card_height = 265

    gap_x = 22
    gap_y = 22

    margin_x = 35
    top = 88

    columns = 3

    rows = max(
        1,
        (len(projects) + columns - 1) // columns,
    )

    height = top + rows * card_height + (rows - 1) * gap_y + 35

    background = colors["background"]
    surface = colors["surface"]
    surface_2 = colors["surface_2"]
    accent = colors["accent"]
    highlight = colors["highlight"]
    text = colors["text"]
    muted = colors["muted"]
    border = colors["border"]
    border_soft = colors["border_soft"]

    parts = []

    parts.append(
        f'''<svg xmlns="http://www.w3.org/2000/svg"
        width="{width}"
        height="{height}"
        viewBox="0 0 {width} {height}"
        role="img"
        aria-label="{escape(title)}">'''
    )

    parts.append(
        f"""
        <defs>

          <linearGradient id="bgGradient"
            x1="0" y1="0"
            x2="1" y2="1">

            <stop offset="0%" stop-color="{background}"/>
            <stop offset="100%" stop-color="{surface_2}"/>

          </linearGradient>

          <linearGradient id="accentGradient"
            x1="0" y1="0"
            x2="1" y2="0">

            <stop offset="0%" stop-color="{accent}"/>
            <stop offset="50%" stop-color="{highlight}"/>
            <stop offset="100%" stop-color="{accent}"/>

          </linearGradient>

          <pattern
            id="grid"
            width="32"
            height="32"
            patternUnits="userSpaceOnUse">

            <path
              d="M32 0H0V32"
              fill="none"
              stroke="{accent}"
              stroke-opacity=".055"
              stroke-width="1"/>

          </pattern>

          <filter
            id="softGlow"
            x="-100%"
            y="-100%"
            width="300%"
            height="300%">

            <feGaussianBlur
              stdDeviation="3"
              result="blur"/>

            <feMerge>
              <feMergeNode in="blur"/>
              <feMergeNode in="SourceGraphic"/>
            </feMerge>

          </filter>

        </defs>
        """
    )

    parts.append(
        f'''
        <rect
          x="0"
          y="0"
          width="{width}"
          height="{height}"
          rx="24"
          fill="url(#bgGradient)"
        />

        <rect
          x="0"
          y="0"
          width="{width}"
          height="{height}"
          rx="24"
          fill="url(#grid)"
        />
        '''
    )

    # Header
    parts.append(
        f'''
        <g>

          <text
            x="35"
            y="40"
            fill="{text}"
            font-family="Inter,Segoe UI,Arial,sans-serif"
            font-size="22"
            font-weight="700"
            letter-spacing="1">

            SELECTED PROJECTS

          </text>

          <text
            x="35"
            y="64"
            fill="{muted}"
            font-family="ui-monospace,SFMono-Regular,Menlo,monospace"
            font-size="10"
            letter-spacing="1.8">

            DIGITAL SYSTEMS • SOFTWARE • TECHNOLOGY

          </text>

          <line
            x1="35"
            y1="74"
            x2="1165"
            y2="74"
            stroke="{border}"
            stroke-opacity=".35"
          />

        </g>
        '''
    )

    if not projects:
        parts.append(
            f'''
            <text
              x="{width / 2}"
              y="160"
              text-anchor="middle"
              fill="{muted}"
              font-family="Inter,Arial,sans-serif"
              font-size="16">

              No projects available.

            </text>
            '''
        )

    for index, project in enumerate(projects):
        row = index // columns
        column = index % columns

        x = margin_x + column * (card_width + gap_x)
        y = top + row * (card_height + gap_y)

        name = truncate(
            project.get("name")
            or project.get("repo_name")
            or "Untitled Project",
            28,
        )

        description = truncate(
            project_description(project),
            72,
        )

        repo_url = project.get(
            "html_url",
            f"https://github.com/{project.get('repo', '')}",
        )

        language = project.get("language") or ""

        tags = project.get("tags") or []

        if language and language not in tags:
            tags = [language] + list(tags)

        tags = tags[:3]

        logo_uri = get_logo(project)

        parts.append(
            f'''
            <a
              href="{escape(repo_url)}"
              target="_blank">

              <g>

                <rect
                  x="{x}"
                  y="{y}"
                  width="{card_width}"
                  height="{card_height}"
                  rx="18"
                  fill="{surface}"
                  stroke="{border_soft}"
                  stroke-width="1"
                />

                <rect
                  x="{x + 1}"
                  y="{y + 1}"
                  width="{card_width - 2}"
                  height="4"
                  rx="2"
                  fill="url(#accentGradient)"
                  opacity=".85"
                />

              </g>
            </a>
            '''
        )

        # Logo
        if logo_uri:
            parts.append(
                f'''
                <rect
                  x="{x + 20}"
                  y="{y + 22}"
                  width="58"
                  height="58"
                  rx="14"
                  fill="{background}"
                  stroke="{border_soft}"
                  stroke-width="1"
                />

                <image
                  x="{x + 29}"
                  y="{y + 31}"
                  width="40"
                  height="40"
                  preserveAspectRatio="xMidYMid meet"
                  href="{logo_uri}"
                />
                '''
            )
        else:
            parts.append(
                f'''
                <rect
                  x="{x + 20}"
                  y="{y + 22}"
                  width="58"
                  height="58"
                  rx="14"
                  fill="{background}"
                  stroke="{border_soft}"
                />

                <circle
                  cx="{x + 49}"
                  cy="{y + 51}"
                  r="6"
                  fill="{accent}"
                  filter="url(#softGlow)"
                />
                '''
            )

        # Project name
        parts.append(
            f'''
            <text
              x="{x + 95}"
              y="{y + 48}"
              fill="{text}"
              font-family="Inter,Segoe UI,Arial,sans-serif"
              font-size="16"
              font-weight="700">

              {escape(name)}

            </text>
            '''
        )

        # Repo
        parts.append(
            f'''
            <text
              x="{x + 95}"
              y="{y + 69}"
              fill="{muted}"
              font-family="ui-monospace,SFMono-Regular,Menlo,monospace"
              font-size="9">

              {escape(project.get("repo", ""))}

            </text>
            '''
        )

        # Description
        parts.append(
            f'''
            <text
              x="{x + 20}"
              y="{y + 116}"
              fill="{muted}"
              font-family="Inter,Segoe UI,Arial,sans-serif"
              font-size="11">

              <tspan
                x="{x + 20}"
                dy="0">

                {escape(description[:55])}

              </tspan>

              <tspan
                x="{x + 20}"
                dy="17">

                {escape(description[55:])}

              </tspan>

            </text>
            '''
        )

        # Tags
        tag_x = x + 20
        tag_y = y + 175

        for tag in tags:
            tag_text = str(tag)
            tag_width = max(
                58,
                len(tag_text) * 6.3 + 22,
            )

            parts.append(
                f'''
                <rect
                  x="{tag_x}"
                  y="{tag_y}"
                  width="{tag_width}"
                  height="25"
                  rx="12.5"
                  fill="{background}"
                  stroke="{accent}"
                  stroke-opacity=".55"
                />

                <text
                  x="{tag_x + tag_width / 2}"
                  y="{tag_y + 16}"
                  text-anchor="middle"
                  fill="{highlight}"
                  font-family="ui-monospace,SFMono-Regular,Menlo,monospace"
                  font-size="8.5"
                  font-weight="600">

                  {escape(tag_text)}

                </text>
                '''
            )

            tag_x += tag_width + 7

        # Bottom metadata
        stars = project.get("stars", 0)
        forks = project.get("forks", 0)

        parts.append(
            f'''
            <text
              x="{x + 20}"
              y="{y + 232}"
              fill="{muted}"
              font-family="ui-monospace,SFMono-Regular,Menlo,monospace"
              font-size="8.5">

              ★ {stars}    FORKS {forks}

            </text>

            <circle
              cx="{x + card_width - 26}"
              cy="{y + card_height - 24}"
              r="4"
              fill="{accent}">

              <animate
                attributeName="opacity"
                values="1;.35;1"
                dur="3.5s"
                repeatCount="indefinite"/>

            </circle>
            '''
        )

    parts.append("</svg>")

    return "\n".join(parts)


def main():
    if len(sys.argv) < 3:
        print(
            "Usage: python generate_projects.py merged.json output_directory"
        )
        sys.exit(1)

    input_file = Path(sys.argv[1])
    output_dir = Path(sys.argv[2])

    output_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    projects = read_projects(input_file)

    dark_svg = create_svg(
        projects,
        DARK,
        "Fajar Adhitia Projects",
    )

    light_svg = create_svg(
        projects,
        LIGHT,
        "Fajar Adhitia Projects",
    )

    dark_output = output_dir / "projects.svg"
    light_output = output_dir / "projects-light.svg"

    dark_output.write_text(
        dark_svg,
        encoding="utf-8",
    )

    light_output.write_text(
        light_svg,
        encoding="utf-8",
    )

    print(f"Generated: {dark_output}")
    print(f"Generated: {light_output}")


if __name__ == "__main__":
    main()
