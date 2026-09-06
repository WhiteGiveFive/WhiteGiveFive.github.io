/**
 * Single source of truth for identity. Everything that appears on more than one
 * page — the name, the positioning line, the link row — is defined here once.
 */
export const site = {
  // DECISION NEEDED: publications are all under "Hongrui Shi"; the spec says
  // "Jimmy Shi". Peers search the former, colleagues use the latter.
  name: 'Hongrui (Jimmy) Shi',
  citationName: 'Hongrui Shi',

  role: 'Postdoctoral Research Associate',
  affiliation: 'University of Lincoln',
  affiliationUrl: 'https://www.lincoln.ac.uk/',

  positioning:
    'Hongrui Shi builds and evaluates computer-vision systems for UK habitat monitoring, with a focus on when their predictions can be trusted.',

  bio: [
    'Leads AI model development for AI-Hab, a NERC-funded collaboration with the UK Centre for Ecology & Hydrology.',
    'PhD from the University of Sheffield on efficiency and heterogeneity in federated learning.',
  ],

  email: 'hshi@lincoln.ac.uk',
  links: [
    { label: 'Google Scholar', url: 'https://scholar.google.com/citations?user=X6z1XHMAAAAJ' },
    { label: 'GitHub', url: 'https://github.com/WhiteGiveFive' },
    { label: 'LinkedIn', url: 'https://www.linkedin.com/in/hongruishi' },
  ],

  cvPdf: '/cv/Hongrui-Shi-CV.pdf',
  photo: '/profile.png',

  // Used for canonical URLs and og: tags from day one (see spec §9 caveat).
  url: 'https://whitegivefive.github.io',
  description:
    'Hongrui Shi — postdoctoral researcher at the University of Lincoln working on computer vision for habitat monitoring and efficient federated learning.',
} as const;

export const nav = [
  { label: 'Research', href: '/research' },
  { label: 'Projects', href: '/projects' },
  { label: 'Notes', href: '/notes' },
  { label: 'Writing', href: '/writing' },
  { label: 'CV', href: '/cv' },
];
