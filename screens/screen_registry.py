from screens.main_menu import MainMenu

# Club screens
from screens.clubs import ClubCreate, ClubView

# Player screens
from screens.players import PlayerEdit, PlayerView

# Tournament screens
from screens.tournament.tournament_menu import TournamentMenu
from screens.tournament.tournament_create import TournamentCreate
from screens.tournament.tournament_actions_menu import TournamentActionsMenu

# Central registry mapping screen names → screen classes
screen_registry = {
    "main-menu": MainMenu,

    # Clubs
    "club-create": ClubCreate,
    "club-view": ClubView,

    # Players
    "player-edit": PlayerEdit,
    "player-view": PlayerView,

    # Tournaments
    "tournament-menu": TournamentMenu,
    "tournament-create": TournamentCreate,
    "tournament-actions": TournamentActionsMenu,
}
