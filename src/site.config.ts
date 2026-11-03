/**
 * Single source of truth for identity. Everything that appears on more than one
 * page — the name, the positioning line, the link row — is defined here once.
 */
export const site = {
  name: 'Hongrui Shi',
  citationName: 'Hongrui Shi',

  role: 'Machine learning researcher',
  affiliation: 'University of Lincoln',
  affiliationUrl: 'https://www.lincoln.ac.uk/',

  positioning: 'Keep learning and building.',

  bio: [
    ['Works in the Applied Vision and Artificial Intelligence Laboratory at the University of Lincoln, leading AI model development for AI-Hab and developing multimodal AI models for habitat monitoring.'],
    [
      'Computer Science PhD from the University of Sheffield on efficient federated learning, supervised by ',
      { label: 'Professor Po Yang', url: 'https://www.sheffield.ac.uk/cs/people/academic/po-yang' },
      ' and ',
      { label: 'Dr Valentin Radu', url: 'https://www.sheffield.ac.uk/cs/people/academic-visitors/dr-valentin-radu' },
      '.',
    ],
  ],

  email: 'hshi@lincoln.ac.uk',
  links: [
    { label: 'Google Scholar', url: 'https://scholar.google.com/citations?user=X6z1XHMAAAAJ' },
    { label: 'GitHub', url: 'https://github.com/WhiteGiveFive' },
    { label: 'LinkedIn', url: 'https://www.linkedin.com/in/hongruishi' },
  ],

  cvPdf: '/cv/Hongrui-Shi-CV.pdf',
  photo: '/profile.jpg',

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
