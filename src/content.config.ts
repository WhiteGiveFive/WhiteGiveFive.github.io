import { defineCollection, z } from 'astro:content';
import { glob, file } from 'astro/loaders';

/**
 * Publications are data, not pages. /research and /cv render from this one
 * collection, so a citation is never edited twice.
 */
const publications = defineCollection({
  loader: file('src/data/publications.json'),
  schema: z.object({
    title: z.string(),
    authors: z.array(z.string()),
    venue: z.string(),
    year: z.number(),
    type: z.enum(['journal', 'conference', 'workshop', 'preprint']),
    pages: z.string().optional(),
    doi: z.string().optional(),
    code: z.string().optional(),
    /** Legacy selection metadata, retained for future curated views. */
    selected: z.number().optional(),
    why: z.string().optional(),
  }),
});

const projects = defineCollection({
  loader: file('src/data/projects.json'),
  schema: z.object({
    name: z.string(),
    subtitle: z.string().optional(),
    blurb: z.string(),
    role: z.string(),
    funding: z.string().optional(),
    outputs: z.array(z.string()).default([]),
    partners: z.array(z.string()).default([]),
    group: z.enum(['current', 'other']).default('other'),
    featured: z.boolean().default(false),
    sortOrder: z.number(),
    /** Honest status beats a stale "active" — spec §6. */
    status: z.enum(['active', 'maintained', 'archived', 'contributed']),
    years: z.string(),
    links: z.array(z.object({ label: z.string(), url: z.string().url() })),
    selected: z.number().optional(),
    why: z.string().optional(),
  }),
});

/** Short, dated, low ceremony. 100-400 words. */
const notes = defineCollection({
  loader: glob({ base: './src/content/notes', pattern: '**/*.{md,mdx}' }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    summary: z.string(),
    tags: z.array(z.string()).default([]),
    draft: z.boolean().default(false),
  }),
});

/** Long-form essays. 800+ words, published when there is something to say. */
const writing = defineCollection({
  loader: glob({ base: './src/content/writing', pattern: '**/*.{md,mdx}' }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    summary: z.string(),
    tags: z.array(z.string()).default([]),
    draft: z.boolean().default(false),
  }),
});

export const collections = { publications, projects, notes, writing };
