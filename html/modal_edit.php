<div id="editProductModal" class="modal fade">
		<div class="modal-dialog">
			<div class="modal-content">
				<form name="edit_product" id="edit_product">
					<div class="modal-header">						
						<h4 class="modal-title">Editar Producto</h4>
						<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
					</div>
					<div class="modal-body">					
						<div class="form-group">
							<label>Código</label>
							<input type="text" name="edit_card_code"  id="edit_card_code" class="form-control" readonly>
							<input type="hidden" name="edit_id" id="edit_id" >
						</div>
						<div class="form-group">
							<label>Cliente</label>
							<input type="text" name="edit_card_nome" id="edit_card_nome" class="form-control" required>
						</div>
						<div class="form-group">
							<label>Fecha</label>
							<input type="date" value="<?php echo date("Y-m-d");?>" name="edit_card_data" id="edit_card_data" class="form-control" required>
						</div>
						<div class="form-group">
							<label>Perfil</label>
							<select readonly="readonly" tabindex="-1" aria-disabled="true" name="edit_card_master" id="edit_card_master" class="form-control">
                                                        <option value=0 selected>Cliente</option>
                                                        <option value=1>Administrador</option>
                                                        </select>
						</div>
						<div class="form-group">
							<label>Contador</label>
							<input type="number" name="edit_card_entradas" id="edit_card_entradas" class="form-control" readonly>
						</div>					
					</div>
					<div class="modal-footer">
						<input type="button" class="btn btn-default" data-dismiss="modal" value="Cancelar">
						<input type="submit" class="btn btn-info" value="Guardar datos">
					</div>
				</form>
			</div>
		</div>
	</div>
