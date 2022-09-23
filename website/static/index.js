function addFavorite(styleID, image, name, link) {
  fetch("/add-favorite", {
    method: "POST",
    body: JSON.stringify({ styleID: styleID, image: image, name: name, link: link}),
  }).then((_res) => {
    window.location.href = "/"
  })
}

function deleteFavorite(favoriteId) {
  fetch("/delete-favorite", {
    method: "POST",
    body: JSON.stringify({ favoriteId: favoriteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

function addNote(note) {
  fetch("/add-note", {
    method: "POST",
    body: JSON.stringify({note: note})
  }).then((_res) => {
    window.location.href = "/";
  });
}

function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}