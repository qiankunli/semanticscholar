from . import Paper


class Author:

    FIELDS = [
        'affiliations',
        'aliases',
        'authorId',
        'citationCount',
        'externalIds',
        'hIndex',
        'homepage',
        'name',
        'paperCount',
        'papers',
        'url'
    ]

    SEARCH_FIELDS = FIELDS

    def __init__(self, data) -> None:
        self._affiliations = None
        self._aliases = None
        self._authorId = None
        self._citationCount = None
        self._externalIds = None
        self._hIndex = None
        self._homepage = None
        self._name = None
        self._paperCount = None
        self._papers = None
        self._url = None
        self._init_attributes(data)

    @property
    def affiliations(self) -> list:
        return self._affiliations

    @property
    def aliases(self) -> list:
        return self._aliases

    @property
    def authorId(self) -> str:
        return self._authorId
    
    @property
    def citationCount(self) -> int:
        return self._citationCount

    @property
    def externalIds(self) -> dict:
        return self._externalIds

    @property
    def hIndex(self) -> int:
        return self._hIndex

    @property
    def homepage(self) -> str:
        return self._homepage

    @property
    def name(self) -> str:
        return self._name

    @property
    def paperCount(self) -> int:
        return self._paperCount

    @property
    def papers(self) -> list:
        return self._papers

    @property
    def url(self) -> str:
        return self._url

    def get_raw_data(self) -> dict:
        return self._data

    def _init_attributes(self, data):
        self._data = data
        if 'affiliations' in data:
            self._affiliations = data['affiliations']
        if 'aliases' in data:
            self._aliases = data['aliases']
        if 'authorId' in data:
            self._authorId = data['authorId']
        if 'citationCount' in data:
            self._citationCount = data['citationCount']
        if 'externalIds' in data:
            self._externalIds = data['externalIds']
        if 'hIndex' in data:
            self._hIndex = data['hIndex']
        if 'homepage' in data:
            self._homepage = data['homepage']
        if 'name' in data:
            self._name = data['name']
        if 'paperCount' in data:
            self._paperCount = data['paperCount']
        if 'papers' in data:
            items = []
            for item in data['papers']:
                items.append(Paper.Paper(item))
            self._papers = items
        if 'url' in data:
            self._url = data['url']
