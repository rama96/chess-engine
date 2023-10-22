(function() {
    document.addEventListener('DOMContentLoaded', function() {
        var board = ChessBoard('board', {
            position: 'start',
            draggable: true,
            pieceTheme: '/static/img/chesspieces/wikipedia/{piece}.png',
            onDrop: function (source, target, piece, newPos, oldPos, orientation) {
                var move = source + '-' + target;

                fetch('/make_move', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ move: move }),
                })
                .then(response => response.json())
                .then(data => {
                    console.log(data);
                })
                .catch(error => {
                    console.error('Error:', error);
                });
            return true;
            }
        });

        var chessboardForm = document.getElementById('chessboard-form');

        chessboardForm.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent the default form submission
        });
    });
})();