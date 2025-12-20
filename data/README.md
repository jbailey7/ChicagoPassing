### DATA SETUP

erDiagram

    GAMES {
        string game_id PK
        int season
        int week
        date gameday
        string home_team
        string away_team
        string stadium
        string roof
        boolean is_dome
        boolean is_soldier_field
    }

    GAME_WEATHER {
        string game_id PK
        float temp_f
        float wind_mph
        boolean precip
    }

    QB_GAME_STATS {
        string game_id FK
        string qb_id
        string qb_name
        string offense_team
        string defense_team
        boolean is_home
        int pass_attempts
        int completions
        int pass_yards
        int interceptions
        int sacks
        int dropbacks
        float epa_sum
        float epa_per_dropback
    }

    DEFENSE_SEASON_STATS {
        int season
        string defense_team
        float def_epa_allowed_per_play_season
    }

    %% Relationships
    GAMES ||--|| GAME_WEATHER : "has"
    GAMES ||--o{ QB_GAME_STATS : "includes"
    DEFENSE_SEASON_STATS ||--o{ QB_GAME_STATS : "opponent season strength"
