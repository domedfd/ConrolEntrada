<?php
	if (empty($_POST['edit_id'])){
		$errors[] = "ID está vacío.";
	} elseif (!empty($_POST['edit_id'])){
	require_once ("../conexion.php");//Contiene funcion que conecta a la base de datos
	// escaping, additionally removing everything that could be (html/javascript-) card_code
    $card_code = mysqli_real_escape_string($con,(strip_tags($_POST["edit_card_code"],ENT_QUOTES)));
	$card_nome = mysqli_real_escape_string($con,(strip_tags($_POST["edit_card_nome"],ENT_QUOTES)));
	$card_data = mysqli_real_escape_string($con,(strip_tags($_POST["edit_card_data"],ENT_QUOTES)));
	$card_master = intval($_POST["edit_card_master"]);
	$card_entradas = floatval($_POST["edit_card_entradas"]);
	
	$id=intval($_POST['edit_id']);
	// UPDATE data into database
    $sql = "UPDATE card SET card_code='".$card_code."', card_nome='".$card_nome."', card_data='".$card_data."', card_entradas='".$card_entradas."',  card_master='".$card_master."' WHERE id='".$id."' ";
    $query = mysqli_query($con,$sql);
    // if product has been added successfully
    if ($query) {
        $messages[] = "El producto ha sido actualizado con éxito.";
    } else {
        $errors[] = "Lo sentimos, la actualización falló. Por favor, regrese y vuelva a intentarlo.";
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
