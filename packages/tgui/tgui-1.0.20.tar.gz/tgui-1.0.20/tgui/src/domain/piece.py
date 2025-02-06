import json
from copy import deepcopy
from typing import List, Union, Optional, Dict, Any

from telebot.types import MessageEntity

from lega4e_library import rdc


class _Piece:

  def __init__(
    self,
    text: str,
    url: str = None,
    type: str = None,
    types: List[str] = None,
    lang: str = None,
    user=None,
  ):
    self.text = text
    self.url = url
    self.user = user
    self.types = {
      val
      for val in [*(types or []), type, None if url is None else 'text_link']
      if val is not None
    }
    self.lang = lang

  def add(
    self,
    type: str = None,
    url: str = None,
    user: str = None,
    lang: str = None,
  ):
    if url is not None:
      self.types.add('text_link')
      self.url = url
    if type is not None:
      self.types.add(type)
    if user is not None:
      self.user = user
    if lang is not None:
      self.lang = lang

  def __repr__(self):
    return f'"{self.text}" ({self.types})'


class Pieces:

  def __init__(self, pieces: List[_Piece] = None, emoji: str = None):
    self.pieces = pieces or []
    self.emoji = emoji

  def toMessage(self):
    return self.toString(), self.getEntities()

  def toString(self):
    return ((f'{self.emoji} ' if self.emoji is not None else '') +
            ''.join([p.text for p in self.pieces]))

  def getEntities(self) -> List[MessageEntity]:
    if self.emoji is not None:
      self.pieces = [_Piece(f'{self.emoji} ')] + self.pieces
    types = rdc(
      lambda a, b: a | b,
      [p.types for p in self.pieces],
      set(),
    )
    entities = rdc(
      lambda a, b: a + b,
      [self.getEntitiesWithType(type) for type in types],
      [],
    )
    if self.emoji is not None:
      self.pieces = list(self.pieces[1:])
    return entities

  def __getitem__(self, key):
    if not isinstance(key, slice):
      raise Exception('Pieces.__getitem__ only with slice')
    length = len(self.toString())
    if key.start is None:
      first, pfirst = 0, 0
    else:
      first, pfirst = self.pieceByPos((key.start + length) % length)
    if key.stop is None:
      last, plast = len(self.pieces) - 1, len(self.pieces[-1].text) - 1
    else:
      last, plast = self.pieceByPos(length -
                                    1 if key.stop >= length else key.stop - 1)
    p = deepcopy(self)
    p.pieces = p.pieces[first:last + 1]
    p.pieces[0].text = p.pieces[0].text[pfirst:None if last !=
                                        first else plast + 1]
    if last != first:
      p.pieces[-1].text = p.pieces[-1].text[:plast + 1]
    return p

  def getEntitiesWithType(self, type: str) -> List[MessageEntity]:
    pos = 0
    entities = []
    for piece in self.pieces:
      text_length = _count_chars(piece.text)
      if type not in piece.types or text_length == 0:
        pos += text_length
        continue
      # if (len(entities) != 0 and
      #     entities[-1].offset + entities[-1].length == pos and
      #     (type != 'text_link' or entities[-1].url == piece.url)):
      #   entities[-1].length += text_length
      # else:
      entities.append(
        MessageEntity(
          type=type,
          offset=pos,
          length=text_length,
          url=piece.url,
          language=piece.lang,
        ))
      pos += text_length
    return entities

  def __add__(self, other):
    if isinstance(other, str):
      return self.__add__(Pieces([_Piece(other)]))
    if isinstance(other, _Piece):
      return self.__add__(Pieces([other]))
    me = deepcopy(self)
    me += other
    return me

  def __iadd__(self, other):
    if isinstance(other, str):
      return self.__iadd__(Pieces([_Piece(other)]))
    if isinstance(other, _Piece):
      return self.__iadd__(Pieces([other]))
    other = deepcopy(other)
    if (len(self.pieces) != 0 and len(other.pieces) != 0 and
        self.pieces[-1].types == other.pieces[0].types and
        self.pieces[-1].url == other.pieces[0].url and
        self.pieces[-1].user == other.pieces[0].user):
      self.pieces[-1].text += other.pieces[0].text
      self.pieces += other.pieces[1:]
    else:
      self.pieces += other.pieces
    self.emoji = other.emoji or self.emoji
    return self

  def pieceByPos(self, pos) -> (int, int):
    p = 0
    for piece in self.pieces:
      length = len(piece.text)
      if p <= pos < p + length:
        return self.pieces.index(piece), pos - p
      p += length
    return -1, -1

  def toDict(self) -> Dict[str, Any]:
    text, entities = self.toMessage()
    values = dict()
    values['text'] = text
    if entities is not None:
      values['entities'] = [e.to_dict() for e in entities]
    else:
      values['entities'] = None
    return values

  def toJson(self, pretty: bool = False) -> str:
    return json.dumps(
      self.toDict(),
      separators=(',', ':') if not pretty else None,
      indent=2 if pretty else None,
      ensure_ascii=False,
    )

  @staticmethod
  def fromDict(data: Dict[str, Any]) -> Any:
    entities = data.get('entities')
    if entities is not None:
      entities = [MessageEntity.de_json(json.dumps(e)) for e in entities]
    return Pieces.fromMessage(data['text'], entities)

  @staticmethod
  def fromJson(s: str) -> Any:
    return Pieces.fromDict(json.loads(s))

  @staticmethod
  def fromMessage(text: str, entities: Optional[List[MessageEntity]]):
    entities = entities or []
    entities = deepcopy(entities)
    p = 0
    for c in text:
      if len(bytes(c, encoding='utf-8')) < 4:
        p += 1
        continue
      for e in entities:
        if e.offset > p:
          e.offset -= 1
        if e.offset <= p < e.offset + e.length:
          e.length -= 1
      p += 1
    p = P(text)
    if entities is None:
      return p
    for entity in entities:
      first, pfirst = p.pieceByPos(entity.offset)
      last, plast = p.pieceByPos(entity.offset + entity.length - 1)
      new1, new2 = None, None
      for i in range(first, last + 1):
        if i == first:
          new1 = deepcopy(p.pieces[first])
          new1.text = new1.text[pfirst:-1 if first != last else plast + 1]
          new1.add(
            type=entity.type,
            url=entity.url,
            user=entity.user.username if entity.user is not None else None,
            lang=entity.language,
          )
        elif i == last:
          new2 = deepcopy(p.pieces[last])
          new2.text = new2.text[:plast + 1]
          new2.add(
            type=entity.type,
            url=entity.url,
            user=entity.user.username if entity.user is not None else None,
            lang=entity.language,
          )
        else:
          p.pieces[i].add(
            type=entity.type,
            url=entity.url,
            user=entity.user.username if entity.user is not None else None,
            lang=entity.language,
          )
      ffirst = deepcopy(p.pieces[first])
      ffirst.text = ffirst.text[:pfirst]
      llast = deepcopy(p.pieces[last])
      llast.text = llast.text[plast + 1:]
      p.pieces = [
        piece for piece in (p.pieces[:first] + [ffirst, new1] +
                            p.pieces[first + 1:last] + [new2, llast] +
                            p.pieces[last + 1:]) if piece is not None
      ]
    return p


def P(
  text: str = None,
  emoji: str = None,
  types: Union[List[str], str] = None,
  url: str = None,
  user=None,
  lang: str = None,
):
  if isinstance(types, str):
    types = [types]
  return Pieces(
    [_Piece(
      text,
      url=url,
      types=types,
      user=user,
      lang=lang,
    )] if text is not None else [],
    emoji=emoji,
  )


def provePiece(p):
  if isinstance(p, Pieces):
    return p
  return P(p)


def _count_chars(text: str) -> int:
  count = 0
  for c in text:
    count += 1 if len(bytes(c, encoding='utf-8')) < 4 else 2
  return count
