import { styled } from "@mui/material/styles";
import Paper from "@mui/material/Paper";
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import { useState } from "react";
import FormControl from "@mui/material/FormControl";
import InputLabel from "@mui/material/InputLabel";
import Select from "@mui/material/Select";
import MenuItem from "@mui/material/MenuItem";
import ToggleButton from "@mui/material/ToggleButton";
import ToggleButtonGroup from "@mui/material/ToggleButtonGroup";

interface SquareState {
	value: "X" | "O" | null;
}

const Item = styled(Paper)<{ player: "X" | "O" | null }>(({ player }) => ({
	width: "150px",
	height: "150px",
	textAlign: "center",
	display: "flex",
	alignItems: "center",
	justifyContent: "center",
	cursor: "pointer",
	boxShadow: "none",
	border: "none",
	fontSize: "64px",
	fontWeight: "bold",
	backgroundColor: "#dadada",
	transition: "background-color 0.3s ease-in-out, color 0.3s ease-in-out",
	...(player === "X" && {
		backgroundColor: "#e3f2fd",
		color: "#2196f3",
	}),
	...(player === "O" && {
		backgroundColor: "#ffebee",
		color: "#f44336",
	}),
	...(player === null && {
		color: "transparent",
		"&:hover": {
			backgroundColor: "#f8f8f8e3",
		},
	}),
}));

export default function ResponsiveGrid() {
	const [estadoPrevisto, setEstadoPrevisto] = useState<string | null>(null);
	const [squares, setSquares] = useState<SquareState[]>(
		Array(9)
			.fill(null)
			.map(() => ({ value: null }))
	);
	const [algoritmo, setAlgoritmo] = useState<string>("arvore");
	const [playerChoice, setPlayerChoice] = useState<"X" | "O">("X");

	console.log("Estado do jogo previsto:", estadoPrevisto);
	const formatTabuleiro = (squares: SquareState[]) => {
		return squares.map((sq) => {
			if (sq.value === "X") return 1;
			if (sq.value === "O") return 0;
			return -1;
		});
	};
	const verificarEstadoDoJogo = async (estado: number[]) => {
		const resposta = await fetch("http://127.0.0.1:8000/prever/", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify({
				estado,
				algoritmo: algoritmo,
			}),
		});
		const dados = await resposta.json();
		return dados.estado_previsto;
	};

	const handlePlayerChange = (
		event: React.MouseEvent<HTMLElement>,
		newChoice: "X" | "O"
	) => {
		if (newChoice !== null) {
			setPlayerChoice(newChoice);
		}
	};

	const handleClick = (index: number) => {
		if (squares[index].value) return; // Se já foi clicado, não faz nada

		const newSquares = squares.map((square, i) => ({
			value: i === index ? playerChoice : square.value,
		}));

		setSquares(newSquares);
		console.log(`Clicked square ${index + 1}, placed ${playerChoice}`);

		const estadoNumerico = formatTabuleiro(newSquares);
		console.log("estaadonumerico", estadoNumerico);

		verificarEstadoDoJogo(estadoNumerico).then((resultado) => {
			setEstadoPrevisto(resultado);
			console.log("Estado do jogo previsto:", resultado);
		});
	};

	const handleRestart = () => {
		setSquares(
			Array(9)
				.fill(null)
				.map(() => ({ value: null }))
		);
	};

	return (
		<Box display="flex" flexDirection="column" alignItems="center" gap="16px">
			<Box display="flex" gap="16px" alignItems="center">
				<FormControl sx={{ minWidth: 200 }}>
					<InputLabel id="algoritmo-select-label">Algoritmo</InputLabel>
					<Select
						labelId="algoritmo-select-label"
						value={algoritmo}
						label="Algoritmo"
						onChange={(e) => setAlgoritmo(e.target.value)}
					>
						<MenuItem value="arvore">Árvore de Decisão</MenuItem>
						<MenuItem value="mlp">MLP</MenuItem>
						<MenuItem value="knn">KNN</MenuItem>
						<MenuItem value="svm">SVM</MenuItem>
					</Select>
				</FormControl>
				<ToggleButtonGroup
					value={playerChoice}
					exclusive
					onChange={handlePlayerChange}
					aria-label="player choice"
				>
					<ToggleButton value="X" aria-label="X">
						X
					</ToggleButton>
					<ToggleButton value="O" aria-label="O">
						O
					</ToggleButton>
				</ToggleButtonGroup>
				<Button
					variant="contained"
					onClick={handleRestart}
					sx={{
						backgroundColor: "#aaaf4c",
						"&:hover": {
							backgroundColor: "#aaaf4c",
						},
					}}
				>
					Start New Game
				</Button>
			</Box>

			{estadoPrevisto && (
				<Box fontSize="24px" fontWeight="bold">
					Estado do jogo: {estadoPrevisto.toUpperCase()}
				</Box>
			)}

			<Box
				display="grid"
				gridTemplateColumns="repeat(3, 150px)"
				margin="auto"
				padding="32px"
				width="fit-content"
				gap="8px"
				borderRadius="8px"
			>
				{squares.map((square, index) => (
					<Item key={index} onClick={() => handleClick(index)} player={square.value}>
						{square.value}
					</Item>
				))}
			</Box>
		</Box>
	);
}
