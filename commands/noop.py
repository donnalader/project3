class NoopCmd:
    def __init__(self, screen_name, clear_context=False, **kwargs):
        self.screen_name = screen_name
        self.clear_context = clear_context
        self.kwargs = kwargs

    def execute(self, app):
        if self.clear_context:
            # Only keep clubs when clearing context
            app.context = {"clubs": app.context.get("clubs", [])}
            app.set_screen(self.screen_name)
        else:
            app.set_screen(self.screen_name, **self.kwargs)



