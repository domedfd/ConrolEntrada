<div id="addProductModal" class="modal fade">
		<div class="modal-dialog">
			<div class="modal-content">
				<form name="add_product" id="add_product">
					<div class="modal-header">						
						<h4 class="modal-title">Agregar Producto</h4>
						<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
					</div>
					<div class="modal-body">					
						<div class="form-group">
							<label>Código</label>
							<input type="text" name="card_code"  id="card_code" class="form-control" required>
							
						</div>
						<div class="form-group">
							<label>Cliente</label>
							<input type="text" name="card_nome" id="card_nome" class="form-control" required>
						</div>
						<div class="form-group">
							<label>Fecha</label>
							<input type="date" value="<?php echo date("Y-m-d");?>" name="card_data" id="card_data" class="form-control" required>
						</div>
						<div class="form-group">
							<label>Perfil</label>
							<select name="card_master" id="card_master" class="form-control">
							<option value=0>Cliente</option>
							<option value=1>Administrador</option>
							</select>
						</div>
						<div class="form-group">
							<label>Contador</label>
							<input type="number" value=0 name="card_entradas" id="card_entradas" class="form-control" readonly>
						</div>					
					</div>
					<div class="modal-footer">
						<input type="button" class="btn btn-default" data-dismiss="modal" value="Cancelar">
						<input type="submit" class="btn btn-success" value="Guardar datos">
					</div>
				</form>
			</div>
		</div>
	</div>
