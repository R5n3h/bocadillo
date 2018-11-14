from orator import Model


class Post(Model):
    """Represents a blog post."""

    __fillable__ = ('title', 'content', 'slug')