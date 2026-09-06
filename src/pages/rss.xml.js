import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import { site } from '../site.config';

export async function GET(context) {
  const notes = await getCollection('notes', ({ data }) => !data.draft);
  const posts = await getCollection('writing', ({ data }) => !data.draft);

  const items = [
    ...notes.map((n) => ({ ...n.data, link: `/notes/${n.id}` })),
    ...posts.map((p) => ({ ...p.data, link: `/writing/${p.id}` })),
  ].sort((a, b) => b.date.valueOf() - a.date.valueOf());

  return rss({
    title: site.citationName,
    description: site.description,
    site: context.site,
    items: items.map((i) => ({
      title: i.title,
      description: i.summary,
      pubDate: i.date,
      link: i.link,
    })),
  });
}
