<svg width="1200" height="420" viewBox="0 0 1200 420" fill="none" xmlns="http://www.w3.org/2000/svg">

  <defs>

```
<!-- Background gradient -->
<linearGradient id="bg" x1="0" y1="0" x2="1200" y2="420" gradientUnits="userSpaceOnUse">
  <stop stop-color="#060B16"/>
  <stop offset="0.5" stop-color="#0A101F"/>
  <stop offset="1" stop-color="#0D1324"/>
</linearGradient>

<!-- Cyan / Purple gradient -->
<linearGradient id="accent" x1="180" y1="100" x2="1000" y2="340" gradientUnits="userSpaceOnUse">
  <stop stop-color="#22D3EE"/>
  <stop offset="0.5" stop-color="#A78BFA"/>
  <stop offset="1" stop-color="#10B981"/>
</linearGradient>

<!-- Soft glow -->
<radialGradient id="glowCyan" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse"
  gradientTransform="translate(930 85) rotate(90) scale(210)">
  <stop stop-color="#22D3EE" stop-opacity="0.20"/>
  <stop offset="1" stop-color="#22D3EE" stop-opacity="0"/>
</radialGradient>

<radialGradient id="glowPurple" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse"
  gradientTransform="translate(1050 360) rotate(90) scale(190)">
  <stop stop-color="#A78BFA" stop-opacity="0.14"/>
  <stop offset="1" stop-color="#A78BFA" stop-opacity="0"/>
</radialGradient>

<!-- Grid -->
<pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse">
  <path
    d="M32 0H0V32"
    stroke="#94A3B8"
    stroke-opacity="0.055"
    stroke-width="1"
  />
</pattern>

<!-- Glow filter -->
<filter id="blurGlow" x="-100%" y="-100%" width="300%" height="300%">
  <feGaussianBlur stdDeviation="5"/>
</filter>

<filter id="softGlow" x="-100%" y="-100%" width="300%" height="300%">
  <feGaussianBlur stdDeviation="12"/>
</filter>

<!-- Clip -->
<clipPath id="clip">
  <rect width="1200" height="420" rx="24"/>
</clipPath>
```

  </defs>

  <!-- ===================================================== -->

  <!-- BACKGROUND                                            -->

  <!-- ===================================================== -->

<rect
 width="1200"
 height="420"
 rx="24"
 fill="url(#bg)"
/>

<rect
 width="1200"
 height="420"
 rx="24"
 fill="url(#grid)"
/>

<rect
 width="1200"
 height="420"
 rx="24"
 fill="url(#glowCyan)"
/>

<rect
 width="1200"
 height="420"
 rx="24"
 fill="url(#glowPurple)"
/>

  <!-- ===================================================== -->

  <!-- BORDER                                                -->

  <!-- ===================================================== -->

<rect
 x="1"
 y="1"
 width="1198"
 height="418"
 rx="23"
 stroke="#334155"
 stroke-opacity="0.55"
/>

<rect
 x="2"
 y="2"
 width="1196"
 height="416"
 rx="22"
 stroke="url(#accent)"
 stroke-opacity="0.12"
/>

  <!-- ===================================================== -->

  <!-- LEFT DECORATION                                       -->

  <!-- ===================================================== -->

  <g opacity="0.6">

```
<circle
  cx="86"
  cy="75"
  r="42"
  stroke="#22D3EE"
  stroke-opacity="0.18"
/>

<circle
  cx="86"
  cy="75"
  r="28"
  stroke="#A78BFA"
  stroke-opacity="0.15"
/>

<circle
  cx="86"
  cy="75"
  r="4"
  fill="#22D3EE"
/>

<path
  d="M86 20V130"
  stroke="#22D3EE"
  stroke-opacity="0.08"
/>

<path
  d="M31 75H141"
  stroke="#22D3EE"
  stroke-opacity="0.08"
/>
```

  </g>

  <!-- ===================================================== -->

  <!-- TOP RIGHT TECH DECORATION                             -->

  <!-- ===================================================== -->

  <g opacity="0.65">

```
<path
  d="M850 45H1085"
  stroke="#22D3EE"
  stroke-opacity="0.15"
/>

<path
  d="M920 58H1125"
  stroke="#A78BFA"
  stroke-opacity="0.10"
/>

<circle
  cx="1090"
  cy="45"
  r="3"
  fill="#22D3EE"
/>

<circle
  cx="1125"
  cy="58"
  r="2"
  fill="#A78BFA"
/>
```

  </g>

  <!-- ===================================================== -->

  <!-- TERMINAL LABEL                                       -->

  <!-- ===================================================== -->

  <g>

```
<rect
  x="120"
  y="88"
  width="190"
  height="32"
  rx="16"
  fill="#0F172A"
  stroke="#334155"
/>

<circle
  cx="140"
  cy="104"
  r="4"
  fill="#10B981"
/>

<text
  x="154"
  y="109"
  fill="#94A3B8"
  font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"
  font-size="12"
  letter-spacing="1.5"
>
  DEVELOPER_PROFILE
</text>
```

  </g>

  <!-- ===================================================== -->

  <!-- MAIN NAME                                            -->

  <!-- ===================================================== -->

<text
x="120"
y="178"
fill="#F8FAFC"
font-family="Inter, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"
font-size="48"
font-weight="700"
letter-spacing="-1.5"

>

```
Fajar Adhitia
```

  </text>

  <!-- Accent line -->

<rect
 x="123"
 y="198"
 width="92"
 height="3"
 rx="1.5"
 fill="url(#accent)"
/>

  <!-- ===================================================== -->

  <!-- ROLE                                                 -->

  <!-- ===================================================== -->

<text
x="120"
y="238"
fill="#22D3EE"
font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"
font-size="16"
font-weight="600"
letter-spacing="1.2"

>

```
SOFTWARE DEVELOPER
```

  </text>

  <!-- ===================================================== -->

  <!-- DESCRIPTION                                          -->

  <!-- ===================================================== -->

<text
x="120"
y="270"
fill="#94A3B8"
font-family="Inter, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"
font-size="14"

>

```
Building web experiences, IoT systems,
```

  </text>

<text
x="120"
y="292"
fill="#94A3B8"
font-family="Inter, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"
font-size="14"

>

```
and intelligent applications.
```

  </text>

  <!-- ===================================================== -->

  <!-- TECH STACK                                           -->

  <!-- ===================================================== -->

  <g>

```
<rect
  x="120"
  y="326"
  width="86"
  height="28"
  rx="14"
  fill="#0F172A"
  stroke="#22D3EE"
  stroke-opacity="0.25"
/>

<text
  x="163"
  y="345"
  text-anchor="middle"
  fill="#67E8F9"
  font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"
  font-size="11"
>
  WEB
</text>


<rect
  x="216"
  y="326"
  width="86"
  height="28"
  rx="14"
  fill="#0F172A"
  stroke="#A78BFA"
  stroke-opacity="0.25"
/>

<text
  x="259"
  y="345"
  text-anchor="middle"
  fill="#C4B5FD"
  font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"
  font-size="11"
>
  IoT
</text>


<rect
  x="312"
  y="326"
  width="86"
  height="28"
  rx="14"
  fill="#0F172A"
  stroke="#10B981"
  stroke-opacity="0.25"
/>

<text
  x="355"
  y="345"
  text-anchor="middle"
  fill="#6EE7B7"
  font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"
  font-size="11"
>
  AI / ML
</text>
```

  </g>

  <!-- ===================================================== -->

  <!-- RIGHT SIDE: ORBITAL SYSTEM                           -->

  <!-- ===================================================== -->

  <g transform="translate(910 220)">

```
<!-- Glow -->
<circle
  cx="0"
  cy="0"
  r="92"
  fill="#22D3EE"
  fill-opacity="0.06"
  filter="url(#softGlow)"
/>

<!-- Main orbit -->
<ellipse
  cx="0"
  cy="0"
  rx="138"
  ry="58"
  transform="rotate(-24)"
  stroke="url(#accent)"
  stroke-opacity="0.32"
  stroke-width="1"
/>

<ellipse
  cx="0"
  cy="0"
  rx="108"
  ry="44"
  transform="rotate(34)"
  stroke="#22D3EE"
  stroke-opacity="0.20"
/>

<ellipse
  cx="0"
  cy="0"
  rx="80"
  ry="34"
  transform="rotate(82)"
  stroke="#A78BFA"
  stroke-opacity="0.20"
/>

<!-- Core -->
<circle
  cx="0"
  cy="0"
  r="28"
  fill="#0F172A"
  stroke="#22D3EE"
  stroke-opacity="0.5"
/>

<circle
  cx="0"
  cy="0"
  r="8"
  fill="#22D3EE"
  filter="url(#blurGlow)"
/>

<circle
  cx="0"
  cy="0"
  r="5"
  fill="#67E8F9"
/>

<!-- Orbit nodes -->
<circle
  cx="120"
  cy="-47"
  r="4"
  fill="#22D3EE"
/>

<circle
  cx="-92"
  cy="48"
  r="4"
  fill="#A78BFA"
/>

<circle
  cx="35"
  cy="77"
  r="3"
  fill="#10B981"
/>

<!-- Satellite lines -->
<path
  d="M-28 0H-154"
  stroke="#22D3EE"
  stroke-opacity="0.16"
/>

<path
  d="M28 0H150"
  stroke="#A78BFA"
  stroke-opacity="0.14"
/>
```

  </g>

  <!-- ===================================================== -->

  <!-- RIGHT LOWER DATA LINES                               -->

  <!-- ===================================================== -->

  <g opacity="0.5">

```
<path
  d="M760 335H1110"
  stroke="#334155"
/>

<path
  d="M790 348H1030"
  stroke="#334155"
/>

<path
  d="M820 361H1080"
  stroke="#334155"
/>

<circle
  cx="1110"
  cy="335"
  r="2"
  fill="#22D3EE"
/>

<circle
  cx="1030"
  cy="348"
  r="2"
  fill="#A78BFA"
/>

<circle
  cx="1080"
  cy="361"
  r="2"
  fill="#10B981"
/>
```

  </g>

  <!-- ===================================================== -->

  <!-- TERMINAL PROMPT                                      -->

  <!-- ===================================================== -->

  <g>

```
<text
  x="760"
  y="115"
  fill="#64748B"
  font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"
  font-size="11"
>
  ~/fajaradhitia
</text>

<text
  x="760"
  y="140"
  fill="#22D3EE"
  font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"
  font-size="12"
>
  $ whoami
</text>

<text
  x="820"
  y="140"
  fill="#F8FAFC"
  font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"
  font-size="12"
>
  fajaradhitia
</text>
```

  </g>

  <!-- ===================================================== -->

  <!-- BOTTOM STATUS                                        -->

  <!-- ===================================================== -->

  <g>

```
<circle
  cx="120"
  cy="385"
  r="4"
  fill="#10B981"
/>

<text
  x="132"
  y="389"
  fill="#64748B"
  font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"
  font-size="10"
  letter-spacing="1"
>
  SYSTEM ONLINE
</text>

<text
  x="1035"
  y="389"
  fill="#475569"
  font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"
  font-size="10"
  text-anchor="end"
>
  FajarAdhitia
</text>
```

  </g>

  <!-- ===================================================== -->

  <!-- DECORATIVE CORNERS                                   -->

  <!-- ===================================================== -->

<path
 d="M24 70V24H70"
 stroke="#22D3EE"
 stroke-opacity="0.4"
/>

<path
 d="M1130 396H1176V350"
 stroke="#A78BFA"
 stroke-opacity="0.35"
/>

</svg>
