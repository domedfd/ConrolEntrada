<?php
	if (empty($_POST['card_nome'])){
		$errors[] = "Ingresa el nombre del producto.";
	} elseif (!empty($_POST['card_nome'])){
	require_once ("../conexion.php");//Contiene funcion que conecta a la base de datos
	// escaping, additionally removing everything that could be (html/javascript-) code
    $prod_card_code = mysqli_real_escape_string($con,(strip_tags($_POST["card_code"],ENT_QUOTES)));
	$prod_card_nome = mysqli_real_escape_string($con,(strip_tags($_POST["card_nome"],ENT_QUOTES)));
	$card_data = mysqli_real_escape_string($con,(strip_tags($_POST["card_data"],ENT_QUOTES)));
	$card_master = intval($_POST["card_master"]);
	

	// REGISTER data into database
    $sql = "INSERT INTO card(id, card_code, card_nome, card_data, card_master) VALUES (NULL,'$prod_card_code','$prod_card_nome','$card_data','$card_master')";
    $query = mysqli_query($con,$sql);
    // if product has been added successfully
    if ($query) {
        $messages[] = "El producto ha sido guardado con éxito.";
    } else {
        $errors[] = "Lo sentimos, el registro falló. Por favor, regrese y vuelva a intentarlo.";
    }
		
	} else 
	{
		$errors[] = "desconocido.";
	}
if (isset($errors)){
			
			?>
			<div class="alert alert-danger" role="alert">
				<button type="button" class="close" data-dismiss="alert">&times;</button>
					<strong>Error!</strong> 
					<?php
						foreach ($errors as $error) {
								echo $error;
							}
						?>
			</div>
			<?php
			}
			if (isset($messages)){
				
				?>
				<div class="alert alert-success" role="alert">
						<button type="button" class="close" data-dismiss="alert">&times;</button>
						<strong>¡Bien hecho!</strong>
						<?php
							foreach ($messages as $message) {
									echo $message;
								}
							?>
				</div>
				<?php
			}
?>
